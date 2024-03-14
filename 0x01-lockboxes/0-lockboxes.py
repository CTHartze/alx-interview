#!/usr/bin/python3
"""Lockboxes"""

def unlockBoxes(boxes):
    """
    Function to determine if all the boxes can be opened.
    :param box_list: List of lists representing the locked boxes.
    :return: True if all boxes can be opened, else False.
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked_boxes = [0]
    for n in unlocked_boxes:
        for key in boxes[n]:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.append(key)

    if len(unlocked_boxes) == len(boxes):
        return True
    return False
