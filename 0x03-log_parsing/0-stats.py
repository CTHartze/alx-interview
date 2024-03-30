#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys

line_count = 0
total_file_size = 0
status_code_counts = {'200': 0,
                      '301': 0,
                      '400': 0,
                      '401': 0,
                      '403': 0,
                      '404': 0,
                      '405': 0,
                      '500': 0}

try:
    for line in sys.stdin:
        line_parts = line.split(' ')
        if len(line_parts) > 2:
            status_code = line_parts[-2]
            file_size = line_parts[-1]
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            total_file_size += int(file_size)
            line_count += 1
            if line_count == 10:
                print('File Size: {:d}'.format(total_file_size))
                sorted_keys = sorted(status_code_counts.keys())
                for key in sorted_keys:
                    value = status_code_counts[key]
                    if value != 0:
                        print('{}: {}'.format(key, value))
                line_count = 0
except Exception:
    pass
finally:
    print('File Size: {:d}'.format(total_file_size))
    sorted_keys = sorted(status_code_counts.keys())
    for key in sorted_keys:
        value = status_code_counts[key]
        if value != 0:
            print('{}: {}'.format(key, value))
