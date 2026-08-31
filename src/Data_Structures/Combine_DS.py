students = [
    {"name": "Amit", "marks": {88, 92, 79}},
    {"name": "Riya", "marks": {95, 95, 60}},
]

for student in students:
    name = student["name"]
    unique_marks = student["marks"]        # already a set, duplicates removed
    average = sum(unique_marks) / len(unique_marks)
    print(name, "-> average:", round(average, 2))
