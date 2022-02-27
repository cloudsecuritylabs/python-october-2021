# # #  List, tuple, set, dict
# #
# my_list = ["1", 2, 3, "apple", "yellow", 10, 15, 20, 200]
# # # print(type(my_list))
# # # print(my_list[-1])
# # # print(my_list[4])
# print(my_list[1:])
# #
# # my_tuple = ("1", 2, 3, "apple", "yellow", 10, 15, 20, 200)
# # print(type(my_tuple))
# # print(my_tuple[-1])
# # print(my_tuple[4])
# # print(my_tuple[::-1])
# #
# # #  ordered? unordered?
# # #  unique keys? duplicate items?
# # #  slice [::-1]?
# # #  add two different data types
# #
# # print(10 + 10)
# #
# # #  membership operator
# #
# # x = 30
# # y = 20
# # result = "x less than y" if x < y else "x greater than y"
# # print(result)
#
#
#
#
#
# # new_list = ["banana", [], {}, 100, 1.1]
#
# my_list = []
# print(len(my_list))
# #
# my_list.append("milk")
# print(my_list)
# #
# my_tuple = tuple(my_list)
# print(type(my_tuple))
#
# # Tuple
# Set
# my_set = { 1, 2, 2, 3 ,4}
# print(my_set)

# my_list = [ 1 ,2 ,3, 4]
# for number in my_list:
#     print(number)


# Dictionary
#
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog' }
# print(a_dict['color'])

#
for key in a_dict:
    print(key)

# for key in a_dict:
#     print(key) # how to print the key?
#
#
# for item in a_dict.items():
#     print(item)
#
for key in a_dict.keys():
    print(key)
#
for value in a_dict.values():
    print(value)

#
# for value in a_dict.values(): print(value)
#
#
#     # print(a_dict[key])
#
# # List
x = [2, 1, 0, -1, -2]
y = [i*i for i in x]
# z = [i*i for i in x]
# #
print(y)
# print(z)



with open("secret_file.txt", "w+") as file:
    file.write("My secret password: P@ssw0rd123")
