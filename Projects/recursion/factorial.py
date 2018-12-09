#!/usr/bin/env python3
import sys

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n-1)

def factloop(n):
    f = n    
    if n <= 1:
        return 1
    else:
        while n > 1:
            f *= n - 1
            n -= 1

    return f



if __name__ == '__main__':
    for n in range(11):
        print(f"{n} : {factorial(n)}")
    
    print()

    for n in range(11):
        print(f"{n} : {factloop(n)}")