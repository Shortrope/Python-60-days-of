# Comprehensions, Iterables and Generators
A comprehension should have no side effects

## Comprehensions
- list
- set
- dict

### List Comprehensions
Readable and expressive way of declaring lists

`[ expr(item) for item in iterable ]`

    >>> quote = "I can think of at least 10 imposible tasks before breakfast".split()
    >>> [len(word) for word in quote]
    [1, 3, 5, 2, 2, 5, 2, 9, 5, 6, 9]

### Set Comprehensions
Same as List Comprehensions but use curly braces
`{ expr(item) for item in iterable }`

    >>> quote = "I can think of at least 10 imposible tasks before breakfast".split()
    >>> {len(word) for word in quote}
    {1, 2, 3, 5, 6, 9}
remember a set contains _unique_ values

### Dict Comprehensions
`{ key_expr:value_expr for item in iterable }`

    country_to_capital = { 'UK': 'London',
                           'Brazil': 'Brazilia',
                           'Moracco': 'Rabat',
                           'Sweden': 'Stockholm'}

    cap_to_country = {capital: country for country, capital in country_to_capital.items()}

## Filtering 
All comprehensions allow an optional filtering clause

`[ expr(item) for item in iterable if predicate(item) ]`

    [len(word) for word in quote if len(word) > 5]
    [len(word) for word in quote if is_long_word(item)]