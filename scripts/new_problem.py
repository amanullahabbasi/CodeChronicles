#!/usr/bin/env python3

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re


TOPIC_ALIASES = {
    "arrays": "Arrays",
    "strings": "Strings",
    "twopointers": "TwoPointers",
    "two-pointers": "TwoPointers",
    "slidingwindow": "SlidingWindow",
    "sliding-window": "SlidingWindow",
    "stack": "Stack",
    "binarysearch": "BinarySearch",
    "binary-search": "BinarySearch",
    "linkedlist": "LinkedList",
    "linked-list": "LinkedList",
    "trees": "Trees",
    "tree": "Trees",
    "heap": "Heap",
    "graphs": "Graphs",
    "graph": "Graphs",
    "backtracking": "Backtracking",
    "dynamicprogramming": "DynamicProgramming",
    "dynamic-programming": "DynamicProgramming",
    "dp": "DynamicProgramming",
    "intervals": "Intervals",
    "greedy": "Greedy",
}


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def normalize_topic(raw_topic: str) -> str:
    key = raw_topic.strip().lower()
    key = key.replace(" ", "").replace("_", "-")
    topic = TOPIC_ALIASES.get(key)
    if topic:
        return topic
    raise SystemExit(f"Unsupported topic: {raw_topic}")


def write_if_missing(path: Path, content: str) -> None:
    if path.exists():
        raise SystemExit(f"File already exists: {path}")
    path.write_text(content, encoding="utf-8")


def build_solution_template(problem: str, topic: str, problem_url: str, today: str) -> str:
    return f'''"""
Problem: {problem}
Link: {problem_url}
Topic: {topic}
Date: {today}

Approach:
- 

Time Complexity:
- O(?)

Space Complexity:
- O(?)

Mistakes / Notes:
- 
"""


class Solution:
    pass
'''


def build_daily_log(problem: str, topic: str, problem_url: str, today: str, difficulty: str) -> str:
    return f"""# Daily Practice Log

- Date: {today}
- Problem: {problem}
- Topic: {topic}
- Difficulty: {difficulty}
- LeetCode URL: {problem_url}
- Solved without AI:
- Time spent:

## First Attempt
- 

## Final Approach
- 

## Complexity
- Time:
- Space:

## Mistakes To Revisit
- 

## Rebuild From Memory
- 
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new daily LeetCode practice file and log.")
    parser.add_argument("--problem", required=True, help="Problem title, for example 'Two Sum'")
    parser.add_argument("--topic", required=True, help="Topic folder, for example Arrays or SlidingWindow")
    parser.add_argument("--url", default="", help="LeetCode problem URL")
    parser.add_argument("--difficulty", default="", help="Easy, Medium, or Hard")
    parser.add_argument("--date", default=str(date.today()), help="Date in YYYY-MM-DD format")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    today = args.date
    topic = normalize_topic(args.topic)
    slug = slugify(args.problem)

    solution_path = repo_root / topic / f"{slug}.py"
    daily_log_path = repo_root / "Daily" / f"{today}-{slug}.md"

    solution_content = build_solution_template(args.problem, topic, args.url, today)
    daily_log_content = build_daily_log(args.problem, topic, args.url, today, args.difficulty)

    write_if_missing(solution_path, solution_content)
    write_if_missing(daily_log_path, daily_log_content)

    print(f"Created solution file: {solution_path}")
    print(f"Created daily log: {daily_log_path}")


if __name__ == "__main__":
    main()
