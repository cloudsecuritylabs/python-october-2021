# sometimes you need to seek for the correct solution
# read a file
# file = open("in-class-example2.txt", "a+")
# # write something to the file
# file.write("Great Python Class 2\n")
# # close the file
# # file.close()
#
# # open the file
# # file = open("in-class-example2.txt", "r")
# file.seek(0)
# content = file.read()
# print(content)


file = open("in-class-example2.txt", "r")
file.seek(0)
# print((file.readlines()[1:]))

# first way
file.seek(0)
for line in file.readlines():
    print(line)

file.seek(0)
# 2nd way
print(file.read())
file.close()



# What happens when you don't close and to read the file again



# basic file
# file = open("myfile.txt", "w+")
# file.write("Most interesting class\n")
# read = file.read()
# # print(read)
# file.close()

#
# # close file please when done
# # file = open("check1.txt", 'a')
# # file.write("Third line\n")
# # file.close()
# myfile = open("check1.txt", 'r')
#
# # myline = myfile.readline()
# # while myline:
# #     print(myline)
# #     myline = myfile.readline()
# # myfile.close()
#
# mylines = myfile.readlines()
# for line in mylines:
#     print(line)
#
# # for line in file:
# #     splitted = line.split(" ")
# #     if splitted[0] == 'First':
# #         print("found")
# #     # print(splitted[0])
#
#
# #
# # file.write("abc")
# # file.write("def")
# # file.writelines("geh")
# # file.writelines("ijk")
# # file.close()
# #
# # file = open("check.txt", 'r')
# # # write content to file
# #
# # print(file.readline(8))
# #
# # # read a file
# # # read a file by line
# #
# # # readline(5) -> reads 5 bytes of a file
# #
# # flush