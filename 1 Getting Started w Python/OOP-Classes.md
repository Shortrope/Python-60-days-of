# OOP = Classes and Why Do We Need Them?
## Class
    class Student:
        def __init__(self, name, id):       # Constructor
            pass

        def __str__(self):
            return "student"

## Attributes
Create in `consturctor`

    def __init__(self, name, student_id=9999):
        self.name = name
        self.student_id = student_id

Or with `setter`

### Class Attribute (static)
Place in the class but not in a method

    class Student:
        school_name = "Springfield High"

        def __init__(self, name, student_id=9999):
            pass

Access class attribs with:

- self.school_name
- Student.school_name

## Inheritance and Polymorphism

## Modules
### Import

    import hs_student
    gina = hs_student.HighSchoolStudent("gina")
    print(gina.get_name_capitalize())

Or

    from hs_student import HighSchoolStudent
    gina = HighSchoolStudent("gina")
    print(gina.get_name_capitalize())

Or

    from hs_student import *