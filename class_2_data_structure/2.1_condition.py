
age = int(input("Please enter your age: "))
if age < 100:
    print("You are too young!")
elif age < 500:
    print("You are little old now")
else:
    print("You must be kidding!")


# interesting and / or behavior for Python
ten = 10
twenty = 20
hundred = 100
print(ten and hundred)
print(ten or hundred)
print(twenty and 100)
print(twenty or ten)


