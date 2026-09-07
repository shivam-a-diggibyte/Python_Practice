import json

student = {"name": "Shivam", "age": 21, "courses": ["Git", "Databricks", "Python"]}

json_string = json.dumps(student, indent=2)
print(json_string)

parsed_back = json.loads(json_string)  # coverts the JSON string back to a Python dictionary
print("Parsed name:", parsed_back["name"])