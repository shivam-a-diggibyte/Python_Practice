with open("notes.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1): # enumerates create a index for each line starting from 1
    print(f"Line {i}: {line.strip()}")
