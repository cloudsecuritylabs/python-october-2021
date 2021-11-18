# Tuple are immutable -- read only
# ORDERED
# ALLOW DUPLICATES
# for a single item tuple, you must add a comma to the end!!
# thistuple = ("apple",)
# print(type(thistuple))
#
# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets

# immutabl
my_tuple = ( 1, 2, 3, 7, 4 )
print(my_tuple[1:4]) #1,2,3,4


my_string = "hundred thousand"
print(my_string[1:4]) #1,2,3,4

# this is still a Tuple
interesting = "Denmark", "Finland", "Norway", "Sweden"
print(type(interesting))


# Under the hood, lists and tuples don’t store data items at all,
# but rather object references.

