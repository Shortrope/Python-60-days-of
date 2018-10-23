# Managing the Filesystem w Python

## `*` parameter
The `*` means the following arguments can only be passed by keyword  

    def do_something(a1, a2, *, a3="Hey", a4=00)

Examples  

    do_something(3, 77)           # Good
    do_something(3, 77, "Hello")  # No
    do_something(3, 77, a4=88")   # Good


## Tuples

- Ordered 
- Immutable

Example:

    t = (33, 44, 55)  
    t[1]    # retruns 44  

### Tuple unpacking
The tuple can be _unpacted_ into separate variables  

    a, b, c = t

The number of variables must match the number of elements in the tuple  

## `os` Module
Operating System system calls  

    import os
    os.getcwd()
    os.chdir("/etc")
    os.listdir("/")         # returns a list
    os.walk("/var/log/")               # recursive list

### `os.stat("file")`
Returns an instance of a stat_result class  
 `<class 'os.stat_result'>`

    info = os.stat("/etc/hosts")
    info                    # displays
    info.st_size

### `os.walk("dir")`
Recursive directory list  
Returns a 3-tuple generator for each directory
- Pathname of the directory
- List of dir names in it
- List of file names in it
