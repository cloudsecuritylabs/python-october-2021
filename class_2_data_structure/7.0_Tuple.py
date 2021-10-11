# Tuple are immutable -- read only
# ORDERED
# ALLOW DUPLICATES
# for a single item tuple, you must add a comma to the end!!
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets