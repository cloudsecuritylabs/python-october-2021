# import a module
import os

# print(os.system("ping -c 4 google.com")) # for linux only

# print(os.listdir("."))
# # os.mkdir("test")
# print(os.getcwd())

# send this info to a text file
# os.system("ping -c 1 google.com > ping.txt")

# mkdir
# rmdir
# rename
# get current dir

# print(os.walk("."))
print(os.stat("."))
# print(os.stat_result)


import os

# os.chdir(".")
# for root, dirs, files in os.walk(".", topdown = False):
#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))



#
# # !/usr/bin/python3
# import os
#
# # showing stat information of file "foo.txt"
# statinfo = os.stat('ping.txt')
#
# print (statinfo)

