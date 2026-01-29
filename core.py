# core.py
"""
Core logic for Interactive DSA Trainer.

Features:
- Algorithm recommendation (rule-based)
- Offline code grading in a restricted sandbox

SECURITY NOTE:
This module uses exec() in a restricted environment for EDUCATIONAL/OFFLINE use only.
Do NOT use with untrusted code in production systems.
"""

import ast
import traceback
from typing import List, Tuple, Any


def ai_recommend_algorithm(problem_text: str) -> str:
    """Return a simple algorithm hint based on keywords."""
    text = problem_text.lower()

    if any(k in text for k in ("sort", "sorted")):
        return "Use Sorting (QuickSort / MergeSort)"
    if any(k in text for k in ("shortest path", "graph")):
        return "Use BFS / Dijkstra"
    if any(k in text for k in ("subarray", "substring")):
        return "Use Sliding Window or Prefix Sum"
    if "tree" in text:
        return "Use DFS / BFS on Tree"
    if "dp" in text or "dynamic" in text:
        return "Use Dynamic Programming"

    return "Try brute force first, then optimize."


def ai_grade_code(
    user_code: str,
    tests: List[Tuple[Any, Any]],
    func_name: str = "solution",
):
    """
    Execute user code in a restricted sandbox and validate against tests.

    Args:
        user_code: Python code defining a function named `solution` by default.
        tests: List of (input, expected_output).
        func_name: Name of the function to test.

    Returns:
        (ok: bool, message: str)
    """
    safe_globals = {
        "__builtins__": {
            "range": range,
            "len": len,
            "print": print,
            "min": min,
            "max": max,
            "sum": sum,
            "enumerate": enumerate,
        }
    }

    try:
        # Syntax check
        ast.parse(user_code)

        # Execute in sandbox
        exec(user_code, safe_globals)

        if func_name not in safe_globals:
            return False, f"Function '{func_name}' not found."

        fn = safe_globals[func_name]

        for inp, expected in tests:
            result = fn(inp)
            if result != expected:
                return False, (
                    f"Failed test: input={inp}, expected={expected}, got={result}"
                )

        return True, "All tests passed ✅"

    except Exception:
        return False, traceback.format_exc()
