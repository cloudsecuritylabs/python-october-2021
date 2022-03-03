# # Key - Value {} PAIR
# # As of Python version 3.7, dictionaries are ordered.
# # In Python 3.6 and earlier, dictionaries are unordered.
#
# my_dict = {
#     "first_name" : "Ankan",
#     "last_name": "Basu"
# }
#
# print(my_dict["first_name"])
#
#
# # Next class -
#
# if "Ankan" in my_dict.keys():
#     print("I found you!")
#
# # del clear
# # del dict

# KEY:VALUE
my_dict = { "http":80, "ssh" : 22, "ftp":21}
print(my_dict["http"])

print(my_dict)
for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

del my_dict["http"]
my_dict.clear()
print(my_dict)


special_tuple = (22,)
print(type(special_tuple))
