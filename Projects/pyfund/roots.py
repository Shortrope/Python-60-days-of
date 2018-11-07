#!/usr/bin/python3

import sys

def sqrt(x):
    '''Compute square roots - Heron method

    Args:
        x: find square root of this number

    Returns:
        square root of x
    
    Raises:
        ValueError: If x is negative
    '''

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("This is never run")
    except ZeroDivisionError:
        print("Cannot compute sqrt of a nefative number!")

    print("Program execution continues normally here.")


def main2():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("This is never run")
    except ZeroDivisionError as e:
        print(e, file=sys.stderr)

    print("Program execution continues normally here.")


if __name__  == '__main__':
    main2()