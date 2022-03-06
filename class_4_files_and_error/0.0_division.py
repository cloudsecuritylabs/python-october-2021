# Try and Except to handle error - 63 built in exceptions
# What happens if num2 =0\
try:
    num1 = 100
    num2 = 10
    math_division = num2 / num1
    print(num1/num2) # DivisionByZero error
    # print(10 + "10")
except:
    print("Something really bad happend!")
else:
    print("All is well")

finally:
    print("Clen up")

raise Exception("OMG!")

#input validation
# asdfasdfsdf


