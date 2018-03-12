file_object = open("/tmp/abc.txt", "r+")
print("File content before writing")

# print(file_object.read())

file_object.write("\nPython is fun and easy!")

file_object.seek(0)
print("File content after writing : ")
print(file_object.read())

file_object.close()