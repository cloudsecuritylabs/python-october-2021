
try:
    num1 = int(input("Please enter a number: "))
    num2 = 20
    div = num2 / num1
    print(div)
except ZeroDivisionError:
    print("Can’t calculate it")
except ValueError:
    print("Please input an integer !")
else:
    print("Everything went well")
finally:
    print("Do the next step!")

# raise("my own error message")
