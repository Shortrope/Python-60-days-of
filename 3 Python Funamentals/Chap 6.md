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


## range
?? a collection rather than a container ??  
Represents an arithmetic sequence of integer  

    range(5)            # stop
    range(5, 10)        # start stop
    range(10, 20, 2)    # start stop step

### enumerate()
Use enumerate() for counters  
enumerate() yields(index,value) tuples

    w = ["hey", "buddy", "goodbye"]
        for p in enumerate(w):
            print(p)

    (0, 'hey')
    (1, 'buddy')
    (2, 'goodbye')

or use tuple unpacking

    for i, p in enumerate(w):
        print("i={0}, p={1}".format(i,p))

## list

    >>> s = "show how to index sequences".split()
    >>> s
    ['show', 'how', 'to', 'index', 'sequences']
    >>> s[2]
    'to'
    >>> s[-2]
    'index'

### slicing

    >>> s[1:3]
    ['how', 'to']
    >>> s[1:-1]
    ['how', 'to', 'index']

### Full copy (shallow copy)
These create a new list but the contents are the same references

   full_copy = s[:]
   full_copy = s.copy()
   full_copy = list(s)      # preferable

See vid 6-6 and 6-7 for full explaination of shallow copy

### repitition

    x = [0] * 5
        [0,0,0,0,0]     # each is a reference to the original '0'!

### remove elements

    del seq[3]
    seq.remove('buddy')

### insert elements

    seq.insert(index, item)

### concatenation

    k = m + n
    K += [1,2,3]
    k.extend([4,5,6])

### reverse and sort

    k.reverse()
    k.sort()
    k.sort(reverse=True)
    k.sort(key)