marks = []
marks.append(78)
marks.append(92)
marks.append(65)
print("Total students:", len(marks))
for m in marks:
    print(m, "-> Pass" if m >= 40 else "-> Fail")
