#!/usr/bin/env python3

file_name = input("Enter a file name: ")

contents = ""
while True:
    new_contents = input("Enter the contents: ")
    if new_contents:
        contents += new_contents + "\n"
    else:
        break

with open(file_name, 'w') as f:
    f.write(contents)
