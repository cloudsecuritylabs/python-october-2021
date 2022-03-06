# get 100 number from a user
# multiple all of them
# print the result

# # 4*4*2*10=???
# try:
#     product = 1
#     while True:
#         for r in range(4):
#             number = int(input("Enter a number: "))
#             product = product * numberexcept:
#         print("Something bad")
# finally:
#     print(product)

# product = 1 * 4 * 10 * 20

product = 1
counter = 0
while True:
    try:
        counter = counter + 1
        number = int(input("Enter a number: "))
        if number==0 or counter == 4:
            break
        product = product * number
    except:
        print("Enter an integer please")
print(product)
