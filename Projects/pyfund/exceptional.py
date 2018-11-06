#!/usr/bin/python3
'''A module for demonstrating exceptions.'''

def convert(s):
    '''Convert to an integer.'''
    try:
        x = int(s)
        print("Success: x =", x)
    except (ValueError, TypeError):
        x = -1
        print("Failed!")
    return x