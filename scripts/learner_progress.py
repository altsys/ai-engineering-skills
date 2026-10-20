#!/usr/bin/env python3
"""Private, atomic learner checkpoints for Linux/macOS. Python standard library only."""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sys
import tempfile


class ProgressError(Exception):
    pass


def validate(checkpoint):
    if not isinstance(checkpoint, dict) or type(checkpoint.get('schema_version')) is not int or checkpoint['schema_version'] != 1:
        raise ProgressError('Expected checkpoint schema_version 1.')
    for key in ('updated', 'goal', 'active_topic', 'next_action'):
        if not isinstance(checkpoint.get(key), str) or not checkpoint[key].strip():
            raise ProgressError(f'Checkpoint requires nonempty {key}.')
    if not isinstance(checkpoint.get('constraints'), list) or not all(isinstance(x, str) for x in checkpoint['constraints']):
        raise ProgressError('constraints must be a list of strings.')
    if not isinstance(checkpoint.get('concepts'), list):
        raise ProgressError('concepts must be a list.')
    seen = set()
    for concept in checkpoint['concepts']:
        if not isinstance(concept, dict):
            raise ProgressError('Each concept must be an object.')
        for key in ('concept', 'current_belief', 'confidence', 'gap_or_uncertainty', 'next_probe'):
            if not isinstance(concept.get(key), str) or not concept[key].strip():
                raise ProgressError(f'Concept requires nonempty {key}.')
        if concept['concept'] in seen:
            raise ProgressError('Duplicate concept names are ambiguous.')
        seen.add(concept['concept'])
        if concept.get('assessment') not in ('untested', 'developing', 'demonstrated', 'needs-recheck'):
            raise ProgressError('Unknown concept assessment.')
        evidence = concept.get('evidence')
        if not isinstance(evidence, list):
            raise ProgressError('evidence must be a list.')
        if concept['assessment'] != 'untested' and not evidence:
            raise ProgressError('Assessed concepts require evidence.')
        for item in evidence:
            if not isinstance(item, dict) or any(not isinstance(item.get(k), str) or not item[k].strip() for k in ('reference', 'observation', 'assistance')):
                raise ProgressError('Evidence requires reference, observation, and assistance.')
    return checkpoint


class Store:
    def __init__(self, root, profile):
        if not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_-]{0,63}', profile):
            raise ProgressError('Use a profile of 1-64 letters, digits, underscores, or hyphens.')
        raw = Path(root).expanduser()
        if raw.is_symlink():
            raise ProgressError('Progress root must not be a symbolic link.')
        self.root = raw.resolve()
        checkout = next((p for p in (self.root, *self.root.parents) if (p / '.git').exists()), None)
        if checkout is not None:
            # A home directory kept in Git (dotfiles) also contains the default root.
            raise ProgressError(f'Progress storage must be outside any Git checkout, but {self.root} is inside {checkout}. '
                                'Set AI_ENGINEERING_PROGRESS_DIR or --root to a private directory outside it.')
        self.directory = self.root / profile
        self.path = self.directory / 'progress.json'

    @contextmanager
    def locked(self):
        try:
            import fcntl
        except ImportError as exc:
            raise ProgressError('This local store requires Linux/macOS file locking.') from exc
        self.root.mkdir(parents=True, exist_ok=True, mode=0o700)
        if self.directory.is_symlink():
            raise ProgressError('Profile must not be a symbolic link.')
        self.directory.mkdir(exist_ok=True, mode=0o700)
        os.chmod(self.directory, 0o700)
        lock = self.directory / '.lock'
        fd = os.open(lock, os.O_CREAT | os.O_RDWR | getattr(os, 'O_NOFOLLOW', 0), 0o600)
        with os.fdopen(fd, 'a') as handle:
            os.chmod(lock, 0o600)
            fcntl.flock(handle, fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(handle, fcntl.LOCK_UN)

    def read(self):
        if self.path.is_symlink():
            raise ProgressError('Checkpoint file must not be a symbolic link.')
        if not self.path.exists():
            return []
        try:
            data = json.loads(self.path.read_text())
            if data['store_version'] != 1 or not isinstance(data['revisions'], list) or not data['revisions']:
                raise ValueError('Invalid store envelope')
            for n, entry in enumerate(data['revisions'], 1):
                if entry['revision'] != n:
                    raise ValueError('Broken revision sequence')
                validate(entry['checkpoint'])
            return data['revisions']
        except (ValueError, KeyError, TypeError, ProgressError) as exc:
            raise ProgressError('Checkpoint store is invalid; preserve it and restore a private backup. Nothing was overwritten.') from exc

    def load(self):
        with self.locked():
            revisions = self.read()
            return {'revision': len(revisions), 'checkpoint': revisions[-1]['checkpoint'] if revisions else None}

    def write(self, revisions):
        # One replacement commits both current state and history, never two independent files.
        fd, temporary = tempfile.mkstemp(prefix='.pending-', dir=self.directory)
        try:
            with os.fdopen(fd, 'w') as handle:
                json.dump({'store_version': 1, 'revisions': revisions}, handle, ensure_ascii=False, indent=2)
                handle.write('\n')
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, self.path)
            directory_fd = os.open(self.directory, os.O_RDONLY)
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)

    def save(self, checkpoint, expected_revision, restore_revision=None):
        with self.locked():
            revisions = self.read()
            if expected_revision != len(revisions):
                raise ProgressError(f'Revision conflict: expected {expected_revision}, current {len(revisions)}. Reload and reconcile before saving.')
            if restore_revision is not None:
                if not 1 <= restore_revision <= len(revisions):
                    raise ProgressError('Restore revision does not exist.')
                checkpoint = revisions[restore_revision - 1]['checkpoint']
            validate(checkpoint)
            entry = {'revision': len(revisions) + 1, 'saved_at': datetime.now(timezone.utc).isoformat(), 'checkpoint': checkpoint}
            if restore_revision is not None:
                entry['restored_from'] = restore_revision
            revisions.append(entry)
            self.write(revisions)
            # Verify persisted data before reporting success.
            verified = self.read()
            if verified[-1] != entry:
                raise ProgressError('Save verification failed; reload before retrying.')
            return {'revision': entry['revision'], 'saved': True, 'path': str(self.path)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', default=os.environ.get('AI_ENGINEERING_PROGRESS_DIR', str(Path.home() / '.local/share/ai-engineering-skills/progress')))
    parser.add_argument('--profile', required=True, help='Stable private learner ID; reuse across topics.')
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('load')
    commands.add_parser('history')
    save = commands.add_parser('save')
    save.add_argument('--expected-revision', type=int, required=True)
    save.add_argument('--input', default='-', help='JSON checkpoint file or - for standard input')
    restore = commands.add_parser('restore')
    restore.add_argument('--revision', type=int, required=True)
    restore.add_argument('--expected-revision', type=int, required=True)
    args = parser.parse_args()
    try:
        store = Store(args.root, args.profile)
        if args.command == 'load':
            result = store.load()
        elif args.command == 'history':
            with store.locked():
                result = [{k: v for k, v in item.items() if k != 'checkpoint'} for item in store.read()]
        elif args.command == 'restore':
            result = store.save(None, args.expected_revision, args.revision)
        else:
            if args.input == '-':
                checkpoint = json.load(sys.stdin)
            else:
                checkpoint = json.loads(Path(args.input).read_text())
            result = store.save(checkpoint, args.expected_revision)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ProgressError, OSError, ValueError) as exc:
        print(f'Progress error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
