#!/usr/bin/python3
"""Lockboxes"""

def unlockBoxes(boxes):
    """
    Function to determine if all the boxes can be opened.
    :param box_list: List of lists representing the locked boxes.
    :return: True if all boxes can be opened, else False.
    """
    unlocked_boxes = [False] * len(boxes)  # Initialize boxes as locked
    unlocked_boxes[0] = True

    for i in range(len(boxes)):
        if unlocked_boxes[i]:
            for key in boxes[i]:
                if key < len(boxes) and not unlocked_boxes[key]:
                    unlocked_boxes[key] = True

    return all(unlocked_boxes)
