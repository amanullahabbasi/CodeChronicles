# CodeChronicles

CodeChronicles is my Python DSA practice workspace. It stores:

- topic-based solution files
- daily practice logs
- reusable templates
- notes on patterns, mistakes, and rebuild-from-memory reviews

## Current Structure

- `Arrays/`
- `Strings/`
- `TwoPointers/`
- `SlidingWindow/`
- `Stack/`
- `BinarySearch/`
- `LinkedList/`
- `Trees/`
- `Heap/`
- `Graphs/`
- `Backtracking/`
- `DynamicProgramming/`
- `Intervals/`
- `Greedy/`
- `Notes/`
- `Daily/`
- `Templates/`
- `scripts/`

## Daily Workflow

1. Create a new problem scaffold.
2. Solve it with a real `No AI First Attempt`.
3. Fill in the matching daily log.
4. Revisit the mistakes and rebuild the solution from memory.

## Create A New Problem

From the repository root:

```bash
./new_problem.sh --problem "Two Sum" --topic Arrays --difficulty Easy --url "https://leetcode.com/problems/two-sum/"
```

This creates:

- `Arrays/two_sum.py`
- `Daily/YYYY-MM-DD-two_sum.md`

You can also set a custom date:

```bash
./new_problem.sh --problem "Best Time to Buy and Sell Stock" --topic Arrays --difficulty Easy --date 2026-05-14
```

## Why This Setup Is Better

- topic folders keep your solved problems organized
- `Daily/` shows consistency over time
- every problem gets both code and written reflection
- the template forces complexity notes and mistake tracking

## Next Useful Habit

After every problem, answer these:

- Could I solve this again without looking?
- What pattern was this really testing?
- What mistake should I avoid next time?
