count = 0
def recur(counter):
    # breaking out of the funtion
    if counter == 10:
        return
    print("*" * counter)
    counter = counter + 1
    recur(counter)

recur(count)


def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number* factorial(number-1)

result = factorial(5)
#5*4*3*2
print(result)



