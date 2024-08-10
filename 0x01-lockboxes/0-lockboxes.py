#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    This function (a method that) determines
    if all the boxes can be opened.

    Args:
    :param boxes: A list of lists, where each sublist represents
    the keys in a box thereby containing keys to other boxes.

    Returns:
    :return: True if all boxes can be opened, or False otherwise.
    """

    # Check if `boxes` is a non-empty list
    if not boxes or type(boxes) is not list or not isinstance(boxes, list):
        # Return False if `boxes` is invalid
        return False

    # Initialize a list to track unlocked boxes, starting with box 0
    unlocked = [0]

    # Iterate over unlocked boxes
    for n in unlocked:
        # Iterate over keys in the current box
        for key in boxes[n]:
            # Check if key is valid and not unlocked
            if key not in unlocked and key < len(boxes):
                # Add the new unlocked box to the list
                unlocked.append(key)

    # Check if all boxes have been unlocked
    if len(unlocked) == len(boxes):
        return True
    return False
