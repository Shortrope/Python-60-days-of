# Chap 6: Collection Types
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
[start, end, stop]

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

### k.sort(key)
`key`: accepts any 'callable' obj... like a function  
The `key` is used to extract items

    h = "not perplexing do handwriting family where I illegibly know doctors".split()
    h.sort(key=len)
    s = ' '.join(h)

This is an 'in place' sort - beware

### sorted()
sorts any iterable and returns a new list

### reversed()
reverses an iterable and returns an iterator - not a list

## Dict
Unordered mapping of 
- unique, immutable keys
- mutable values

### Keys
Must be immutable :  str, numbers, tuples 

### Constructor
Can convert other types to a dict
`dict()` constructor accepts:
- iterable of key-value pairs as 2-tuples
- keword arguments
- mapping like another dict

    names_ages = dict([('Shaggy', 22), ('Daphnie', 30)])
    phonetic = dict(a='alfa', b='bravo', c='charlie')
    mapping = dict(phonetic)

### shallow copy
    sc = d.copy()
    dsc = dict(d)   # pass an existing dict to the constructor

### concatination
    nd = d.update(md)
    If duplicate keys, the new values are used  

    for key in colors:
        print("{key} -> {value}".format(key=key, value=colors[key]))

    for value in colors.values():
    for key in colors.key():
    for key, value in colors.item():    # iterates over tuples

### `in` and `not in`
Only operates on the keys

### Remove items
    del colors['blue']

### Pretty printing 
    from pprint import pprint as pp

    pp(mydict)

## set
- unordered, mutable collection
- unique, immutable objects

Uses `{ }` like a dict but contains single items  
Create an empty `set` w its constructor  

    e = set()

Sets can be constructed from any iterable  
Duplicates are discarded!

    t = [1,4,1,2,5,7,7]
    s = set(t)      
    >>> [1,4,2,5,7]

- in, not in
- s.add(9)
- s.update([12,23,45])
- s.remove(23)
- s.discard(23)     # no error if not in
- t = s.copy()      # shallow
- t = set(s)        # shallow copy

### Set Algebra
    blue_eyes.union(blond_hair)                 # all blue_eys and all blond_hair
    blue_eyes.intersection(blond_hair)          # all with blue_eys and blond_hair
    blue_eyes.difference(blond_hair)            # all with blue_eys and not blond_hair
    blue_eyes.symmetric_difference(blond_hair)  # all with blue_eys or blond_hair but not both

    blue_eyes.issubset(blond_hair)              # are all blue_eyes also in blond_hair
    blue_eyes.issuperset(blond_hair)            # ??
    blue_eyes.isdisjoint(blond_hair)            # no members in common
    

## Collection Protocols
Set of operations or methods that a type must support

| Protocol         | Collection type                           |
|------------------|-------------------------------------------|
| Container        | str, list, range, tuple, bytes, set, dict |
| Sized            | str, list, range, tuple, bytes, set, dict |
| Iterable         | str, list, range, tuple, bytes, set, dict |
| Sequence         | str, list, range, tuple, bytes, set, dict |
| Mutable Sequence | list                                      |
| Mutable Set      | set                                       |
| Mutable Mapping  | dict                                      |

_Container_:  Tesing w `in` and `not in`  
_Sized_:  `len()`  
_Iterable_: Can produce an iterable.. `for in`  
_Sequence_: Items can be retrieved with an integer index.. 

    item = a[2]
    index = a.index(item)
    ?? num = a.count(item)
    num = len(d)
    r = reversed(a)
