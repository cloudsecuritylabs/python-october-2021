# there are four types of scope
# local
# global
# built-in
# enclosed

# global scope
txt = "Print that"
def test0():
    #local variable
    global txt
    txt = " print something new"
    print(txt)

test0()
print(txt)

# # a global variable can be accessed from with a function
# # but the variable cannot be changed
# name = "john"
#
# def test():
#     txt="Print this"
#     name = "Basu" # how to use global?
#     print(txt)
#     print(name)
#
# test()
# # print(txt)
# print(name)