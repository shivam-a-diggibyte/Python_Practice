import json
from pathlib import Path

# Get the folder where this Python file is located
file_path = Path(__file__).parent / "employee.json"

# Read JSON file
with open(file_path, "r") as file:
    employee = json.load(file)

print("Employee Name:", employee["name"])
print("Department:", employee["department"])
print("Skills:", employee["skills"])

# Add another skill
employee["skills"].append("Databricks")

# Write updated JSON
with open(file_path, "w") as file:
    json.dump(employee, file, indent=4)

print("JSON file updated successfully.")