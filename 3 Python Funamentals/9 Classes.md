# Classes

Class names use CamelCase

    class CamelCase:

To create an instance of the class, use the constructor:

    c = CamelCase()

`self` is the first arg to all instance methods  
`self` is a reference to the instance object  
`__init__` instance method for initializing new objects  
`__init__` is an _initializer_, not a _constructor_  
`__init__` configures an instance after it is created but before it is called.
`__init__` is used by the constrctor  
private methods and attributes should be prefixed with an underscore  
Its all public. No enforcement of private and protected members.  



    class Flight:

        def __init__():
            self._number = number

        def number(self):
            return "1234"

`class invariants` are established in the __init__

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))
        if not number[2:].isdigit():
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
