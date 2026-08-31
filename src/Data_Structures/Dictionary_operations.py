student = {"name": "Shivam", "age": 21}

print(student.keys())          # dict_keys(['name', 'age'])

print(student.get("course"))   # None — no error, key doesn't exist

student.update({"course": "Python"})

for key, value in student.items():
    print(key, "->", value)

