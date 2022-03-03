# create a list  --
# ORDERED
# ALLOW DUPLICATES
#https://www.w3schools.com/python/python_ref_list.asp
# Create a list for common ports
common_ports = [ 80, 443, 123, 3389, 53, 25, 110 ]
# how to print type of the variable?
print(type(common_ports))
# how to print list?
print(common_ports)
# Print the length of the list
print(len(common_ports))
# Print a sorted list
# common_ports.sort()
# print(common_ports)
# print(sorted(common_ports))

# List index starts at 0
print(common_ports[0])
print(common_ports[6])
print(common_ports[-1])

# get the first item from port list
# print the last item from the port list


# # add (append) an item to the list
# common_ports.append(22)
# print(common_ports)
#
# # remove an item from the list
# common_ports.remove(123)
# print(common_ports)
#
# # remove and store the removed item (pop)
#
# removed_port= common_ports.pop()
# print(removed_port)
# print(common_ports)
#
# # if IP in list, print yes
# if 3389 in common_ports:
#     print("I found the port")
# else:
#     print("Not found")

# SLICING: list[a:b] with skip
# The search will start at index a (included) and end at index b (not included).

#[80, 443, 123, 3389, 53, 25, 110]
print(common_ports[::5])

# Delete a list
del common_ports

print(common_ports)

# list can have mixed types of data types. Create a mixed list for common ports and protocols
























# my_list1 = []
# print(type(my_list1))
# my_list2 = [ "Apple" , "banana", 100, 1000.99, ["another", "list"]]
# my_list3 = [ 1, 2, 3, 4]
# print(my_list3[::2])  #0,1,2,3
# print(my_list3[0])
# print(my_list3[-2])
# my_list3.append(5)
# my_list3.remove(2)
# removed_item = my_list3.pop()
# print(my_list3)
# print(removed_item)

# del(my_list3[2])
# my_list3[2] = 10
# print(my_list3)

# print(my_list3[0])
# print(my_list3[3])

# print(len(my_list3))
# print(my_list3[4])
#
#
# thislist = list(("apple", "banana", "cherry"))

# create a list with some items
# the list() constructor thislist = list(("apple", "banana", "cherry")) # note the double round-brackets

# populate list

# Access List - List index (first item, last item, range of items)


# list[a:b]
# The search will start at index a (included) and end at index b (not included).

# sort a list

# delete list
# del my_list

# print(my_list)

