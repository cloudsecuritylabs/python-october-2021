# an instance of a class is aware of the class it is from
# variables defined in a class are available to the instances
# the attribute is not located int he instance, it is located in the class!


# empty class
class MyClass(object):
    pass
    # var = 20 # can you print from instance?

this_object1 = MyClass()
print(this_object1)
print(type(this_object1))
print (this_object1.var)

print()


this_object2 = MyClass()
print(this_object2)
print(type(this_object2))

