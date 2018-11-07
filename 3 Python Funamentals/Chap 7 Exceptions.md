# Chap 7: Exceptions

File: _exceptional.py_

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

Callers need to know what exceptions to expect and when.  
Use exceptions that users will anticipate.  
Standard exceptions are often the best choice.  
Detect a pre condition early and raise an exception there... e.g. check for 0  

    if x < 0:
        raise ValueError("Cannot compute sqrt of neg num {}".format(x))

Can add a list of exceptions expected in the doc-string for the function  
... see roots.py  

`try...finally` lets you clean up whether an exception occurs or not.  
The `finally` block is executed not matter how the `try` block exits  

    import os

    def make_at(path, dir_name):
        original_path = os.getcwd()
        try:
            os.chdir(path)
            os.mkdir(dir_name)
        except OSError as e:
            print(e, file=sys.stderr)
            raise
        finally:
            os.chdir(original_path)