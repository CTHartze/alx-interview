#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys


def print_metrics(status_code_dict, total_size):
    """
    Function to print metrics
    Args:
        status_code_dict: dictionary of status codes
        total_size: total size of the file
    Returns:
        None
    """
    print("Total File Size: {}".format(total_size))
    for code, count in sorted(status_code_dict.items()):
        if count != 0:
            print("{}: {}".format(code, count))


"""Initialization"""
total_size = 0
current_code = 0
line_counter = 0
status_code_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

"""Processing input"""
try:
    for line in sys.stdin:  # loops through line
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]  # reverses list

        if len(parsed_line) > 2:
            line_counter += 1

            if line_counter <= 10:
                total_size += int(parsed_line[0])
                current_code = parsed_line[1]

                if current_code in status_code_dict.keys():
                    status_code_dict[current_code] += 1

            if line_counter == 10:
                print_metrics(status_code_dict, total_size)
                line_counter = 0

finally:
    print_metrics(status_code_dict, total_size)
