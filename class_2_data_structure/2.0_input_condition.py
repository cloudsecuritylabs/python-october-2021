# Relational Operators
# 1. Equality Operator (==)
# 2. Greater than (>) >=
# 3. Less than (<) <=
# 4. Not Equal !=


# similar to lab 1
# get user age
# if age < 100, print too young!
# type casting



# Precision is a problem
# always remember not to compare numbers directly!
is_true = (18.0 == 18.000000000000001)
print(f"{is_true}")

is_true = (18.0 == 18.01)
print(f"{is_true}")

test = 5 == 5
print(test)
print(type(test))