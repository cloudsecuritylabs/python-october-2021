'''
- safe storage of data in an instance
- allow data access only via instance methods
- data must be validated
'''

class MyEncapsulationExample(object):
    # two arguments - setter method
    def set_value(self, value):
        # we can add code for input validation?
        self.value = value

    # getter methods
    def get_val(self):
        return self.value

## instantiate class
e1 = MyEncapsulationExample()
e2 = MyEncapsulationExample()

e1.set_value(20)
e2.set_value(30)

print(e1.get_val())
print(e2.get_val())

e1.value = 3000
print(e1.get_val())