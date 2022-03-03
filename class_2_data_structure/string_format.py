'''
string format lab
'''
name = "John"
age = 24
my_string = "My name is %s and my age is %d" % (name, age ) # C style
print(my_string)

my_string = "My name is {} and my age is {}".format(name, age) # python style
print(my_string)

my_string = f"My name is {name} and my age is {age}" # python style - Basu prefers
print(my_string)