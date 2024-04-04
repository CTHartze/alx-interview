#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Checks if given data set represents a valid UTF-8 encoding"""
    bytes_to_process = 0
    
    for byte in data:
        if bytes_to_process == 0:
            mask = 0b10000000
            while mask & byte:
                bytes_to_process += 1
                mask >>= 1

            if bytes_to_process == 0:
                continue

            if bytes_to_process == 1 or bytes_to_process > 4 or byte >> 6 != 0b10:
                return False
        else:
            if byte >> 6 != 0b10:
                return False

        bytes_to_process -= 1

    if bytes_to_process != 0:
        return False

    return True
