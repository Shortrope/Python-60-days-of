# Functions, Files, Yield and Lambda

## Functions

    def func_name(arg1, arg2):
    def func_name(arg1, arg2=10):     # default value
    def func_name(*args):             # variable num of args
    def func_name(name, *args):       # variable num of args
    def func_name(name, **kwargs):    # variable num of KeyWord args


Return

    def get_students_titlecase():
      students_titlecase = []
      for student in students:
        students_titlecase = student.title()
      return students_titlecase

Parameters

    def add_student(name):
      students.append(name)

## Nested Functions and Closures
Nested functions are allowed

## Open, Read, Write Files
### Opening Files

    f = open("filename", "access mode")
access modes
- "w" - Writing: overwrites entire file
- "r' - Reading a text file
- "a" - Appending to a new or existing file
- "rb" - Reading a binary file
- "wb" - Writing to a binary file

### Writing to files

    f.write(var + "\n")
    f.close()

### Reading files
_readlines()_ returns a list

    f = open("students.txt", "r")
    for stud in f.readlines():
      ...