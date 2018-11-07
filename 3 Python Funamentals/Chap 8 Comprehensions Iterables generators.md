# Comprehensions, Iterables and Generators

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

    cap_to_country = {capital: country for country in country_to_capital.items()}