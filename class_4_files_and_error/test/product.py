try:
    product = 1
    number = int(input("Give me a number: "))
    for n in range(1, number + 1):
        product = product * n
    print(product)
except ValueError:
    print("give me an integer please ")
