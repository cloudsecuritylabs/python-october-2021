

# file = open("file-demo-append.txt", "w+")
# for i in range(10,15,2):
#     file.write("this is line " + str(i) + "\n")
# file.close()

# file = open("file-demo-append.txt", "r")
# # content = file.read()
# # print(content)
# rl = file.readlines()
# for line in rl:
#     print(line, end= "")
# file.close()


with open("with-format.hacked", "w+") as file:
    file.write("Another way to handle files")

with open("with-format.hacked", "r") as file:
    print(file.read())


