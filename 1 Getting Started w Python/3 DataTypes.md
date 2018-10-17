# Python Data Types

## Integers and floats

    answer = 43
    pi = 3.14159
    antswer + pi

cast

    int(pi) == 3
    float(answer) == 42.0

## String

    'Hello World'  == "Hello World" == """Hello World"""
    "hello".capitalize() == "hello"
    "hello".replace("e", "a") == "hallo"
    "hello".isalpha() == True
    "123".isdigit() == True
    "some,csv,values".split(",") == ["some", "csv", "values"]

    print("The lazy " + animal + " jumps over the big'ol " + color + " cow!")
    print("The lazy {0} jumps over the big'ol {1} cow!".format(animal, color))
    print(f"The lazy {animal} jumps over the big'ol {color} cow!")
    print(r"The lazy {animal} jumps over the big'ol {color} cow!")

Can use """ for multi line comments

### String Format function

    name = "Josie"
    machine = "HAL"
    "Nice to meat you {0}. I am {1}".format(name, machine)
    f"Nice to meat you {name}. I am {machine}"

## Boolean

    isAntlet = True
    isZpool = False
    int(isAntlet) == 1
    int(isZpool) == 0
    str(isAntlet) == "True"

    aliens_found = None   # like Null

## If statements

    num = 5
    if num == 5:
      print("Nubmer is 5")
    else:
      print("Number is not 5")

### Truthy Falsy

0     Falsy
1..   Truthy
""    Falsy
"hey" Truthy

### Not If

    if number != 5:
      ...

    isAntlet = True
    if not isAntlet:
      ...

### And Or

    if x > 21 and y < 1:
      ...

    if num == 5 or isAntlet:
      ...

### Ternary If Statements  

    a = 1
    b = 2
    "bigger" if a > b else "smaller"

## Lists

    names = []
    names = ["Josie", "Scobby", "Shaggy"]
    names[0] == "Josie"
    names[-1] == "Shaggy"
    names.append("Homer")
    "Josie" in names == True
    len(names) == 3
    del names[1]
    names[1:] == ["Scobby", "Shaggy"]
    names[1:-1] == ["Scobby"]

## Loops
### For loops

    for name in student_names:
      print("Student name is {0}".format(name))

Assumes increment by 1 to the end of list

    x = 0
    for i in range(10):
      x += 10
      print ("x: {0}".format(x))

`range()` : use for range and step size

    range(10) == [0, 1, 2, .. 9]
    range(5, 10) == [5, 6, .. 9]
    range(5, 10, 2) == [5, 7, 9]

## Break and Continue

## While Loops
Must inc counter

    x = 0
    while x < 10:
      print("x: {0}".format(x))
      x += 1

Infinite Loop

    while True:
      if x:
        break

## Dictionaries
Key Value pairs
Just like JSON obj

    student = {
      "name": "Josie",
      "id": 1413,
      "feedback": None
    }

    student["name"]

Avoid error if key does not exist

    student["lastName"] == KeyError
    student.get("lastName", "Unknown") == "Unknown"

    student.keys() == ["name", "id", "feedback"]
    student.values() == ["Josie", "1413", None]

    del student["name"]

List of Dictionaries

    students = [
      {"name"": "Josie", "id": 1413", "feedback": None},
      {"name"": "Mario", "id": 1414", "feedback": None},
      {"name"": "Mary", "id": 1415", "feedback": None},
    ]

    student[0]["name"]

## Exceptions
When to use Exception handling?  

- Using files
- Getting user input

    student = {
      "name": "Josie",
      "id": 1413,
      "feedback": None
    }

    try:
      student["lastName"]
      numName = 3 + student["lastName"]
    except KeyError:
      print("Error finding lastName")
    except TypeError as error:
      print("Error: Can't add those together!")
      print(error)
    except Exception:
      print("Unknown Error!")

    print("This code executes")

## Other datatypes

- complex
- bytes
- bytearray
- tuple
- set
- frozenset


