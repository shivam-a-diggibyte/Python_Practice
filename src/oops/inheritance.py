class Person:
    def __init__(self,name):
        self.name=name

    def introduce(self):
        print(f"Hello, my name is: {self.name}")

class employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary

employee_1=employee("Shivam",100000)
employee_1.introduce()