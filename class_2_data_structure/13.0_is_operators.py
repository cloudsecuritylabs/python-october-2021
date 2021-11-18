a = ["cat", "dog", "parrot"]
b = ["cat", "dog", "parrot"]
print(a is b)


c = "something"
d = None
answer = c is not None,  d is None
print(answer)
print(type(answer))


a = 1
b = 2
c = 3
d = 3
e = 4

result = a is b, c == d, e > 5
print(result)
print(type(result))
print(result[2])


number = 10
print (5<=number<=20)

# Membership operator
list1 = [1,2,3,4,5]
if 2 in list1:
    print("yes")