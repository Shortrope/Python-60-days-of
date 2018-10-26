# Command Line Arguments

## sys.argv
`import sys`  
sys.argv is a list of each string, space separated, from the cli

    myutil -t apple go

sys-argv[0] == myutil  
sys-argv[1] == -t  
sys-argv[2] == apple  
sys-argv[3] == go  

## Argument parsing Modules
- **optparse**
- getopt    - older module
- argparse  - newer module

optparse

    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-v", "--verbose",
                      dest="verbose",
                      help="Display verbose output")
    parser.add_option("-p", "--port",
                      dest="port",
                      type="int"
                      default=80
                      help="Port number to forward")

    (options, args) = parser.parse_args()

The 'dest' is the variable in which that option value will be stored  
`options`: dict containing values for the options  
`args`: List containting positional arguments  

Option actions:
- store
- store_true, store_false
- store_const
- append - append the arg to a list

**Store**  
`store` is the default action  
Make sure the arg is the correct type  
And store in specific variable

    parser.add_option("-f", "--file",
                  action="store", type="string", dest="filename")

`string` is the default type

    parser.add_option("-f", "--file",
                  dest="filename")

**Booleans**  
Set options.verbose to True w -v  
Set options.verbose to False w -q  

    parser.add_option("-v", action="store_true", dest="verbose")
    parser.add_option("-q", action="store_false", dest="verbose")

**Default** values

    parser.add_option("-v", action="store_false", dest="verbose", default=True)

Or use set_defaults()

    parser.set_defaults(verbose=True)


## optparse documentation
https://docs.python.org/3/library/optparse.html

