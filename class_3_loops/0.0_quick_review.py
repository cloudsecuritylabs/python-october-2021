# List
# Tuple
# Set
# Dictionary

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key) # how to prin the key?


for item in a_dict.items():
    print(item)


for value in a_dict.values(): print(value)


    # print(a_dict[key])

# List
x = [2, 1, 0, -1, -2]
y = [i*i for i in x if i<0]
z = [i*i for i in x]

print(y)
print(z)