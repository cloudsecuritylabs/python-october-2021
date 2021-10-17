
# basic file
# file = open("myfile.txt", "b")


#close file please when done
# file = open("check1.txt", 'a')
# file.write("\n")
# file.write("Third line ")
# file.close()
file = open("check1.txt", 'r')
for line in file:
    splitted = line.split(" ")
    if splitted[0] == 'First':
        print("found")
    # print(splitted[0])


#
# file.write("abc")
# file.write("def")
# file.writelines("geh")
# file.writelines("ijk")
# file.close()
#
# file = open("check.txt", 'r')
# # write content to file
#
# print(file.readline(8))
#
# # read a file
# # read a file by line
#
# # readline(5) -> reads 5 bytes of a file
#
# # flush