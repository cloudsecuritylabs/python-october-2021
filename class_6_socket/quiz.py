# if True:
#     print("Hello")

# X = 10
# if True or False:
#     X = X + 10
# print(X)


#
# interesting_list = ["a", "Cat", 1000, 66]
# # for item in interesting_list:
# #     print(item)
# import os
# length_of_list = len(interesting_list)
#
# i = 0
# while i < length_of_list:
#     print(interesting_list[i])
#     i = i + 1
#
# def main():
#     print("My main method")

x = 10

def func():
    global x
    x = 20

func()
print(x)