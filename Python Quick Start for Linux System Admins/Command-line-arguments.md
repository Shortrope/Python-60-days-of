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