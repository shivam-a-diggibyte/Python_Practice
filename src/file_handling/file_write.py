with open("notes.txt", "w") as f:
    f.write("Hello, this is line 1.\n") #use to write content to the file

    f.write("This is line 2.\n") # overwrite the existing content in the file

print("File written.")

with open("notes.txt", "r") as f:
    content = f.read() #use to read content from the file
print(content)