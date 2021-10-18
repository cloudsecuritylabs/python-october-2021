# A method on an instance passes "instance" as the
# first argument to the method, known as self
import random
class Greetings(object):
    greeting = 'Hello world!'

    #
    def greet_me(self): # what happens if we take the self out?
        print('Hello world')
        print(self)

    def random_num(self):
        self.rand = random.randint(1,10)

# instantiate the class
greet = Greetings()
print(greet.greeting)
greet.greet_me()
# greet.random_num() # we must run this line of code first before accessing greet.rand
# here, the attribute is not part of the class, it is part of the instance
# this is just like accessing a class variable
print(greet.rand)

# what will happen???
# print(greet.greet_me())