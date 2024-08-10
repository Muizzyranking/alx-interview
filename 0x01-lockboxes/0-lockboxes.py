#!/usr/bin/python3
"""
Method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened.

    Args:
      boxes: A list of lists representing the keys in each box.

    Returns:
      True if all boxes can be opened, False otherwise.
    """

    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # First box is unlocked

    def dfs(box):
        visited[box] = True
        for key in boxes[box]:
            if not visited[key]:
                dfs(key)

    dfs(0)
    return all(visited)
