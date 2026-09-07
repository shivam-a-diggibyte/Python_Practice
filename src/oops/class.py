class car:
    # class have 2 types things stored in it 
    a= 12                            # 1. Attributes 
    def hello():
        print('hello, how are you ?') # 2. Methods



class Student:
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age        # attribute

    def greet(self):          # method
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

s1 = Student("Shivam", 21)
print(s1.greet())
print("Name:", s1.name, "| Age:", s1.age)
