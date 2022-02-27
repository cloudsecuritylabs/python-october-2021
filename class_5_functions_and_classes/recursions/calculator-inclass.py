# goal is to create a calculator
# addition, subtraction
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

calculation_type = input("Input + for addition, - for subtraction, * for multiplication, and / for division: ")
num1 = int(input("Please give the first number: "))
num2 = int(input("Please give the second number: "))


def calculator(mathtype, number1, number2):
    #logic to do calculation
    result = 0
    if calculation_type == "+":
        result = addition(number1, number2)
    elif calculation_type == "-":
        result = subtraction(number1, number2)
    elif calculation_type == "*":
        result = multiplication(number1, number2)
    elif calculation_type == "/":
        result = division(number1, number2)
    return result


# result = 0
# if calculation_type == "+":
#     result = addition(num1,num2)
# elif calculation_type == "-":
#     result = subtraction(num1,num2)
# elif calculation_type == "*":
#     result = multiplication(num1,num2)
# elif calculation_type == "/":
#     result = division(num1,num2)

print(calculator(calculation_type, num1, num2))



# print(addition(4,2))
# print(subtraction(4,2))
# print(multiplication(4,2))
# print(division(4,2))





