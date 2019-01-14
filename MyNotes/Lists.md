# Lists

## Methods:

    .append(item)       # append to the end of the list  
    .extend(iterable)   # append all items from the iterable  
    .insert(i, item)    # insert 'item' at index 'i'  

    .clear()            # removes all items from the list  
    del list[i]         # remove an item by index
    del list[2:4]       # remove slice
    del list[:]         # remove all items
    .pop(i)             # remove and return the item at index 'i'  
    .remove(item)       # remove the first occurance of 'item'  

    .copy()             # returns a shallow copy  
    .count(item)        # number of time 'item' appears in the list  
    .index(item, start, end)    # index of first occurance of 'item'  
    .reverse()          # in-place reverse items  
    .sort(key=None, reverse=False)    # in-place sort  

## Deep copy

    from copy import deepcopy

    list1 = [[1,2], [3,4,5]
    list2 = deepcopy(list1)

## Sorting
list.sort() is only for Lists  
sorted() can be used w any iterable

    list.sort(key=None, reverse=False)           # in-place sort  
    sorted(iterable, key=None, reverse=False)    # returns a new sorted list

Key is a function that takes a single argument and returns a key for sorting  

    sorted(names, key=str.lower)
    sorted(student_tuples, key=lambda student: student[2])
    sorted(student_objs, key=lambda student: student.age)

### Sorting w Operator Module Functions
itemgetter()  
attrgetter()  
methodcoller()  

    from operator import itemgetter, attrgetter

    sorted(student_tuples, key=itemgetter(2))
    sorted(student_objs, key=attrgetter('age'))

Multiple levels of sorting with these operators  

    sorted(student_tuples, key=itemgetter(2,0))
    sorted(student_objs, key=attrgetter('age', 'name'))


## Stacks and Queues
### Stacks  

    list.append(x)
    list.pop(x)

### Queue
for queues use `collections.deque`

    from collections import deque
    q = deque(['joe', 'jose'])
    q.append('josie')
    q.popleft()


## List Comprehensions

    squares = [x**2 for x in range(10)]

With an `if` filter 

    >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]