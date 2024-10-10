#!/usr/bin/python3
""" Determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Check if all the boxes can be opened
    Args:
        boxes (list): List of boxes
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    opened = set()

    def search(box):
        if box in opened:
            return
        opened.add(box)

        for key in boxes[box]:
            search(key)

    search(0)

    return len(opened) == len(boxes)

