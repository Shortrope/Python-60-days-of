# PDB Python DeBugger

    import pdb
    pdb.set_trace()
    help
    help continue
    import pdb; pdb.set_trace()

Run the script w the debugger

    python3 -m pdb palindrome.py

show current line

    (Pdb) where

Next Line

    (Pdb) next

Run the script without 'next'ing

    (Pdb) cont
    ^C              # to break out of continous loop

Show surrounding code at current location in script

    (Pdb) list

?

    (Pdb) return

Exit Pdb: may nee to run 'exit' a few times to exit

    (Pdb) exit

## Break point
You can add a break point to the script with

    import pdb: pdb.set_trace()

## View Vars
Just print the variables

    print x

