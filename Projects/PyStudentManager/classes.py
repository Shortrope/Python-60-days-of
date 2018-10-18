students = []

class Student:
    def __init__(self, name, student_id=9999):
        student = {"name": name, "student_id": student_id}
        students.append(student)

    def __str__(self):
        return "student"


fay = Student("Fay")
print(fay)