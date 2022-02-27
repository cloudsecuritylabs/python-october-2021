first_num = int(input("Please enter the first number: "))
second_num = int(input("Please enter the second number: "))
operator = input("Please enter one of the following operators: +, -, *, / :")

def add(first_num, second_num):
    return first_num + second_num

def div(first_num, second_num):
    return first_num / second_num

def sub(first_num, second_num):
    return first_num - second_num

def mul(first_num, second_num):
    return first_num * second_num

def calculate(first_num, second_num):
    if operator == "+":
        print(add(first_num, second_num))
    if operator == "-":
        print(sub(first_num, second_num))
    if operator == "/":
        print(div(first_num, second_num))
    if operator == "*":
        print(mul(first_num, second_num))


calculate(first_num,second_num )
