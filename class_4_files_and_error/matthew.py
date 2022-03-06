file = open("in-class-example2.txt", "a+")
file.write("Great Python Class 4\n") # add \n at the end of the file to create a new line

# close the file
# file.close()

# open the file
# file = open("in-class-example2.txt", "r")
file.seek(0)
# read and print file using read() method
content = file.read()
print(content)