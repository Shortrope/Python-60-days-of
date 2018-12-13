#!/usr/bin/env python3

def display_message(message, x):
    print((message + " ") * x)

message = input("Enter a message: ")
num = int(input("message x :"))

display_message(message, num)
