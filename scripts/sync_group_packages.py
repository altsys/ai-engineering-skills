#!/usr/bin/env python3
"""Build the four standalone group skills from the coach's canonical topic guides."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
COACH = SKILLS / "ai-engineering-coach"
GROUPS = {
    "ai-engineering-foundations": {
        "title": "AI Engineering Foundations",
        "short_description": "LLM behavior, prompting, and model choice",
        "description": "Teach LLM behavior, prompting, and model choice through adaptive diagnosis and experiments. Use when a learner is building a foundation for practical AI engineering.",
        "topics": ("llm-fundamentals", "prompting-structured-outputs", "model-selection"),
    },
    "ai-engineering-knowledge-systems": {
        "title": "AI Engineering Knowledge Systems",
        "short_description": "Embeddings, retrieval, and grounded answers",
        "description": "Teach embeddings, retrieval, and RAG through adaptive diagnosis and experiments. Use when a learner is building or debugging grounded AI applications.",
        "topics": ("embeddings", "retrieval", "rag"),
    },
    "ai-engineering-agents": {
        "title": "AI Engineering Agents",
        "short_description": "Tool use, agent workflows, and safe failures",
        "description": "Teach tool calling, agent workflows, and safe failure handling through adaptive diagnosis and experiments. Use when a learner is building AI systems that take actions.",
        "topics": ("tool-calling", "agents-workflows", "safety-failure-handling"),
    },
    "ai-engineering-production": {
        "title": "AI Engineering Production",
        "short_description": "Evaluation, operations, and system design",
        "description": "Teach evaluations, observability, latency, deployment, and system design through adaptive diagnosis and experiments. Use when a learner is operating or designing production AI systems.",
        "topics": ("evals", "observability", "latency-cost", "serving-deployment", "production-ai-system-design"),
    },
}


def main() -> None:
    bundled = [topic for group in GROUPS.values() for topic in group["topics"]]
    canonical = {path.name for path in (COACH / "topics").iterdir() if path.is_dir()}
    if len(bundled) != len(set(bundled)) or set(bundled) != canonical:
        raise SystemExit("Group topics must cover every coach topic exactly once")
    for name, group in GROUPS.items():
        target = SKILLS / name
        target.mkdir(exist_ok=True)
        for folder in ("shared", "resources", "scripts"):
            shutil.copytree(COACH / folder, target / folder, dirs_exist_ok=True)
        catalog = target / "resources" / "catalog.md"
        catalog_text = catalog.read_text(encoding="utf-8")
        for other in (p.name for p in (COACH / "topics").iterdir() if p.is_dir()):
            if other not in group["topics"]:
                catalog_text = catalog_text.replace(
                    f"[{other}](../topics/{other}/TOPIC.md)", other
                )
        catalog.write_text(catalog_text, encoding="utf-8")
        for topic in group["topics"]:
            source = COACH / "topics" / topic / "TOPIC.md"
            destination = target / "topics" / topic / "TOPIC.md"
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        links = "\n".join(f"- [{topic}](topics/{topic}/TOPIC.md)" for topic in group["topics"])
        (target / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: {group['description']}\n---\n\n"
            f"# {group['title']}\n\n"
            "Read [teaching principles](shared/teaching-principles.md), "
            "[learner model](shared/learner-model.md), and "
            "[progress storage](shared/progress-storage.md) before teaching. "
            "Use the bundled `scripts/learner_progress.py` with one stable private profile. "
            "Load before teaching, save after meaningful changes and before handoff, "
            "and verify each save. If durable storage is unavailable, provide a portable checkpoint.\n\n"
            "Diagnose the learner's goal and current mental model, then read the relevant topic guide:\n\n"
            f"{links}\n\n"
            "Treat these topics as a scope map, not a fixed lesson order. "
            "Use a prediction, debugging task, or experiment to find the smallest useful gap. "
            "Use the [resource catalog](resources/catalog.md) only after diagnosing that gap; "
            "verify the exact source and section before assigning it. "
            "Record observed evidence and assistance, preserve contradictions, and update only the affected learner-model claims. "
            "Keep the same learner profile when moving to another group or the coach.\n",
            encoding="utf-8",
        )
        agents = target / "agents"
        agents.mkdir(exist_ok=True)
        (agents / "openai.yaml").write_text(
            "interface:\n"
            f"  display_name: \"{group['title']}\"\n"
            f"  short_description: \"{group['short_description']}\"\n",
            encoding="utf-8",
        )
        print(f"Updated {name}")


if __name__ == "__main__":
    main()
