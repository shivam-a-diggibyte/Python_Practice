import os

filename = "notes.txt"
missing_file = "does_not_exist.txt"

if os.path.exists(filename):
    print(f"{filename} exists.")
else:
    print(f"{filename} does not exist.")

try:
    with open(missing_file, "r") as f:
        f.read()
except FileNotFoundError:
    print(f"Could not open {missing_file} — it doesn't exist.")
