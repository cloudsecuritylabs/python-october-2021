# there are four types of scope
# local
# global
# built-in
# enclosed

def test0():
    txt="Print this"
    print(txt)


# a global variable can be accessed from with a function
# but the variable cannot be changed
name = "john"

def test():
    txt="Print this"
    name = "Basu" # how to use global?
    print(txt)
    print(name)

test()
# print(txt)
print(name)