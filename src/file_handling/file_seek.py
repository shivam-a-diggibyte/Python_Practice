with open("file.txt", "w") as f:
    f.write("Hello, this is line 1.\n") #use to write content to the file

    f.write("This is line 2.\n")    

print("File written.")

with open ("file.txt", "r") as f:
    content = f.read() #use to read content from the file
    f.seek(4)
    content_after_seek = f.read()
    print("Content after seek:", content_after_seek)