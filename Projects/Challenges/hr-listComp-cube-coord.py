#!/usr/bin/python3
from pprint import pprint as pp

x = input("x: ")
y = input("y: ")
z = input("z: ")
n = input("n: ")

coords = [ [i,j,k] for i in range(int(x)+1) for j in range(int(y)+1) for k in range(int(z)+1) if i+j+k != int(n) ]

pp(coords)
