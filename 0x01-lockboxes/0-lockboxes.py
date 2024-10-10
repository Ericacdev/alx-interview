#!/usr/bin/python3
"""
Lockboxes problem solution
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for m in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = m in boxes[idx] and m != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
