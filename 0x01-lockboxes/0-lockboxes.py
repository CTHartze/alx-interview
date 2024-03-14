#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened starting from (box 0).

    :param boxes: List of lists representing locked boxes.
    :return: True if all boxes can be opened, else False.
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
