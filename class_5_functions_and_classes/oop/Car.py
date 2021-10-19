class Car:

    # create a constructor
    def __init__(self):
        self.color = "white"
    #
    # def set_color(self, color):
    #     self.color = color


# create an object
car1 = Car()
print(car1.set_color("Blue"))

print(car1.color)
print(car1)

car2 = Car()
car2.color = "red"
print(car2.color)
print(car2)

