students = []

class Student:
    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=9999):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student: " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):
    school_name = "Springfield High"

#    def get_school_name(self):
#        return "This is a High School Student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + " - HS"


fay = Student("fay")
print(fay.get_name_capitalize())
print(fay.get_school_name())
print(Student.school_name)

print()

gina = HighSchoolStudent("gina")
print(gina.get_name_capitalize())
print(gina.get_school_name())
print(HighSchoolStudent.school_name)
