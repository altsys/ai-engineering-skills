import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/learner_progress.py'
spec = importlib.util.spec_from_file_location('progress', SCRIPT)
progress = importlib.util.module_from_spec(spec)
spec.loader.exec_module(progress)


def checkpoint():
    return {'schema_version': 1, 'updated': 'test', 'goal': 'Build a tool app', 'constraints': [], 'active_topic': 'tool-calling', 'concepts': [], 'next_action': 'Probe retries'}


class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'private'
        self.store = progress.Store(self.root, 'learner-a')

    def test_new_save_resume_handoff_and_history(self):
        self.assertEqual(self.store.load(), {'revision': 0, 'checkpoint': None})
        first = checkpoint()
        self.store.save(first, 0)
        second = copy.deepcopy(first)
        second['active_topic'] = 'agents-workflows'
        second['next_action'] = 'Probe recovery'
        self.store.save(second, 1)
        self.assertEqual(progress.Store(self.root, 'learner-a').load()['checkpoint'], second)
        self.assertEqual(self.store.read()[0]['checkpoint'], first)
        self.assertEqual(os.stat(self.store.path).st_mode & 0o777, 0o600)
        self.assertEqual(os.stat(self.store.directory).st_mode & 0o777, 0o700)

    def test_concurrent_writers_do_not_lose_updates(self):
        command = [sys.executable, str(SCRIPT), '--root', str(self.root), '--profile', 'learner-a', 'save', '--expected-revision', '0']
        processes = [subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) for _ in range(2)]
        results = [p.communicate(json.dumps(checkpoint())) for p in processes]
        self.assertEqual(sorted(p.returncode for p in processes), [0, 1])
        self.assertTrue(any('Revision conflict' in error for _, error in results))
        self.assertEqual(self.store.load()['revision'], 1)

    def test_failed_replace_preserves_old_state(self):
        self.store.save(checkpoint(), 0)
        before = self.store.path.read_bytes()
        with patch.object(progress.os, 'replace', side_effect=OSError('disk error')):
            with self.assertRaises(OSError):
                self.store.save(checkpoint(), 1)
        self.assertEqual(self.store.path.read_bytes(), before)
        self.assertFalse(list(self.store.directory.glob('.pending-*')))

    def test_corruption_is_not_silently_reset(self):
        self.store.save(checkpoint(), 0)
        self.store.path.write_text('{broken')
        with self.assertRaises(progress.ProgressError):
            self.store.save(checkpoint(), 1)
        self.assertEqual(self.store.path.read_text(), '{broken')

    def test_restore_creates_new_revision_and_keeps_history(self):
        first = checkpoint()
        self.store.save(first, 0)
        second = dict(first, next_action='Different next probe')
        self.store.save(second, 1)
        self.store.save(None, 2, restore_revision=1)
        self.assertEqual(self.store.load(), {'revision': 3, 'checkpoint': first})
        self.assertEqual(self.store.read()[1]['checkpoint'], second)

    def test_profiles_are_isolated(self):
        self.store.save(checkpoint(), 0)
        self.assertIsNone(progress.Store(self.root, 'learner-b').load()['checkpoint'])

    def test_invalid_input_cannot_overwrite(self):
        self.store.save(checkpoint(), 0)
        bad = checkpoint()
        bad['schema_version'] = 2
        with self.assertRaises(progress.ProgressError):
            self.store.save(bad, 1)
        self.assertEqual(self.store.load()['revision'], 1)

    def test_paths_cannot_escape_or_enter_repo(self):
        with self.assertRaises(progress.ProgressError):
            progress.Store(self.root, '../other')
        repo = Path(self.temp.name) / 'repo'
        repo.mkdir()
        (repo / '.git').write_text('gitdir: elsewhere')
        with self.assertRaises(progress.ProgressError):
            progress.Store(repo / 'progress', 'learner')

    def test_cli_reports_verified_save_and_load(self):
        command = [sys.executable, str(SCRIPT), '--root', str(self.root), '--profile', 'learner-a']
        saved = subprocess.run(command + ['save', '--expected-revision', '0'], input=json.dumps(checkpoint()), capture_output=True, text=True, check=True)
        self.assertTrue(json.loads(saved.stdout)['saved'])
        loaded = subprocess.run(command + ['load'], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(loaded.stdout)['checkpoint'], checkpoint())


if __name__ == '__main__':
    unittest.main()
