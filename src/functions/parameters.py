def student_details(name, age):  #practiced positional arguments
    print("Name:", name)
    print("Age:", age)


student_details("Shivam", 25)

def student_details(name, age): #keyword arguments
    print("Name:", name)
    print("Age:", age)


student_details(age=25, name="Shivam")

def greet(name="Student"): #default parameter
    print(f"Hello, {name}!")


greet()
greet("Shivam")