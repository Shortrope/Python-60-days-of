# Iteration and Generators

'for' loops and 'comprehensions' are most common ways to perform _iteration_

- `iterable` objects - protocol
- `iterator` objects - protocol

## iterable
`iter()` function takes an iterable obj and returns an _iterator_

    iterator = iter(iterable)

## iterator
`next()` functioin takes an iterator and returns the 'next' item

    item = next(iterator)

Example:

    >>> iterable = ['hey', 'hello', 'whatsAhp']
    >>> iterator = iter(iterable)
    >>> next(iterator)
    'hey'
    >>> next(iterator)
    'hello'
    >>> next(iterator)
    'whatsAhp'
    >>> next(iterator)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration

## Generators
**Lazily** evaluated iterable sequences
Can handle infinite sequences w no definite end
- streams of data
- active log files

Defined by a function having
- at least one `yield` statement
- a return statement w no args
- or an implicit return at the end

**A Generator returns a new `generator` object**

    >>> def gen123():
    ...   yield 1
    ...   yield 2
    ...   yield 3def
    >>> g = gen123()
    >>> g
    <generator object gen123 at 0x7f97f760dbf8>
    >>> next(g)
    1
    >>> next(g)
    2
    >>> next(g)
    3
    >>> next(g)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration
    >>>
    >>> g = gen123()
    >>> g
    <generator object gen123 at 0x7f97f760dbf8>
    >>> for x in g:
    ...   print(x)
    ...
    1
    2
    3

## Stateful Generators

## Generator Comprehensions
List comprehensions use square brackets '[ ]'  
Set and Dict comprehensions use curly braces '{ }'  
Gererator comprehensions use parenthesis '( )'  

`(expr(item) for item in iterable)`