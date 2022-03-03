# GOAL - check if a customer can buy alcohol / >= 21 years of age
# get user input for name
name = input("What is your name? ")
# get user input for age
age = input("what is your age? ")

# print name and age
print(f'hello {name} you are {age} years old!')

# create conditionals
# if age >= 21 --> Print that you can buy alcohol

# can_i_buy_alcohol = (int(age) >= 21)

if int(age) >= 21:
    print("You can enjoy some alcohol!")
else:
    print("Sorry, you need to wait.")
# else --> print you cannot




















# name = input("What is your name? ")
# age = input("What is your age? ")
# age = int(age)
# print("Hello {}, your age is {}".format(name, age))
# if age >= 21:
#     print("You can buy an alcoholic beverage")
# else:
#     print("You cannot buy an alcoholic beverage")
#
# input("\nPress 'Enter' to exit this program.")