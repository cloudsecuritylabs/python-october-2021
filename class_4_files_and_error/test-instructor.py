
f = open("myfile1.txt", "w") # create the file if it does not exist
for i in range(5):
    f.write('This is a line ' + str(i) + "\n")
f.close()


f = open("myfile.txt", "r")
# print(f.read())
# f.seek(0)
# rl = f.readlines()
# for line in rl:
#         print(line, end="")

f.seek(0)
first_two = f.readlines(2)
for i in first_two:
    print(i)

f.close()