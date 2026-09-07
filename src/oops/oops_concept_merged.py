from abc import ABC, abstractmethod

class employee(ABC):

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @abstractmethod
    def bonus(self):
        pass
    def introduce(self):
        print(f"Hello, my name is: {self.name} and my salary is: {self.salary}")

class developer(employee):
    super().__init__(name,salary)

    def bonus(self):
        return self.salary*0.1

class manager(employee):
    super().__init__(name,salary)

    def bonus(self):
        return self.salary*0.3


developer1=developer("Shivam",100000)
manager1=manager("Amit",200000)

developer1.introduce()
manager1.introduce()