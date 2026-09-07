def print_info(**kwargs):

    for key, value in kwargs.items():

        print(key, "=", value)


print_info(name="Shivam", age=21, course="Python")

def student_info(name, **details): #kwargs with normal parameters
    print("Name:", name)
    print("Details:", details)


student_info(
    "Shivam",
    age=21,
    course="Python",
    city="Bangalore"
)