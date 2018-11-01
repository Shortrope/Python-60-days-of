# Chap 6
## Main Topics
- Built-in Collection Types
- Protocols that Unite the Collections

Collections:
- tuple
- str
- range
- list
- dict
- set

## Tuple
_Immutable sequence of arbitrary objects_
 
- Like a list but delimited with parentheses ( )
- Element access: zero indexed - mytup[0]
- Lenth: len(mytup)
- Iterate with `for` loop
- Concat w `+` operator
- Repetition w `*` operator

An empty tuple:

    ()

For a single item tuple must have a comma 

    (329,)

Parentheses can be ommitted. Return statement can return a tuple

    return "hey", "buddy"

### Tuple unpacking

    point = (5,7)
    x, y = point

### Swap variables

    a, b = b, a

### create a tuple from an iterable using tuple constructor

    mytup = tuple([123,456,678,90])
    mychars = tuple("Hey Buddy")

### Test Contains

    456 in mytup
    'a' not in mychars

## str
_Immutable sequence of characters (Unicode codepoints)_

    len(s)
    "Hey" + "Buddy"

### .join()

    y = ':'.join('name', 'port', 'IP', 'passwd')
        'name:port:IP:passwd'

### .split()

    y.split(':')
        ['name', 'port', 'IP', 'passwd']

### .partition()
returns the prefix, separator, suffix  
Use tuple unpacking  

    'unforgetable'.partition('forget')
        ('un', 'forget', 'able')

The '_' underscore is used for unused or dummy values

    hostport, _, antletport = '8080:80'.partition(':')

### .format()

    "The age of {0} is {1}".format('Jane', 24)

Access keys or indexes

    pos = (65.3, 23.1, 82.2)
    "Position x={pos[0]} y={pos[1]} z={pos[2]}".format(pos=pos)

with math

    import math
    "Math constants: pi={m.pi:.3f}, e={m.e:.3f}". format(m=math)