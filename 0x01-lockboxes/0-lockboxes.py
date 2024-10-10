#!/usr/bin/python3
"""
0-lockboxes module
Determines if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    opened_boxes = set()
    opened_boxes.add(0)
    keys = boxes[0]
    
    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys.extend(boxes[key])
    
    return len(opened_boxes) == len(boxes)

