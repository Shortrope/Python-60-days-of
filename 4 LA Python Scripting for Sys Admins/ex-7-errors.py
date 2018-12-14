#!/usr/bin/env python3

import sys

try:
    file_name = sys.argv[1]
    line_number = int(sys.argv[2])

except IndexError:
    print("Missing argument(s). Please supply the file name and line number.")
    print("     Usage: ex-7-errors.py file_name line_number")

sys.exit(1)

try:
    with open(file_name, 'r') as f:
        lines = f.readlines()
    print(lines[line_number - 1])

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist!")
except IndexError:
    print(f"The file '{file_name}' does not contain {line_number} lines.")
