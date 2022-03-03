from decimal import *
answer = 0.1 + 0.1 + 0.1 - 0.3
print(answer)


a = Decimal('0.1')
b = Decimal('0.3')
print(a + a + a - b)

#
#
# # # # be very careful when comparing numbers!
# is_true = ("18.0" == "18.00000000000000000001")
# print(f" {is_true}")# GOAL - check if a customer can buy alcohol / >= 21 years of age
# # get user input for name
# name = input("What is your name? ")
# # get user input for age
# age = input("what is your age? ")
#
# # print name and age
# print(f'hello {name} you are {age} years old!')
#
# # create conditionals
# # if age >= 21 --> Print that you can buy alcohol
#
# # can_i_buy_alcohol = (int(age) >= 21)
#
# if int(age) >= 21:
#     print("You can enjoy some alcohol!")
# else:
#     print("Sorry, you need to wait.")