# for loop in Python

# end for print
for i in range(5):
    print(i)
    # print(i, end="*")


# create a list
my_mixed_bag = ["1", 2, "Three", 4, "5" ]
# loop for x in list print some stuff

# print(','.join(my_mixed_bag))

# works same way as


names = ['Philip', 'Lise', 'Bond']
counts = [len(n) for n in names]
print(counts)