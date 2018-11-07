#!/usr/bin/python3
'''A module for demonstrating exceptions.'''

import sys
from math import log

def convert(s):
    '''Convert to an integer.'''
    try:
        x = int(s)
    except (ValueError, TypeError):
        x = -1
    return x


def convert2(s):
    '''Convert to an integer. Handle with exception object'''
    try:
        x = int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}"\
               .format(str(e)), file=sys.stderr)
        raise
    return x


def string_log(s):
    '''be careful when returning error codes and not raising exceptions'''
    v = convert3(s)
    return log(v)