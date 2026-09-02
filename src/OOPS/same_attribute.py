# two objects sharing the same class attributes.
class Student:
    school = "DigiByte Academy"   # class attribute — shared

    def __init__(self, name):
        self.name = name          # instance attribute — unique

s1 = Student("Amit")
s2 = Student("Riya")
print(s1.name, "studies at", s1.school)
print(s2.name, "studies at", s2.school)
