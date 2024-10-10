#!/usr/bin/python3
"""
Determines if all the boxes can be opened
"""



def canUnlockAll(boxes):
"""
set to keep track of opened boxes
"""
    opened_boxes = set()
    opened_boxes.add(0)
    keys = boxes[0]

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys.extend(boxes[key])

    return len(opened_boxes) == len(boxes)
