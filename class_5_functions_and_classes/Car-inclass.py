class Car:
    def __init__(self, color="black", window_number=2, price=0):
        self.color = color
        self.window_number = window_number
        self.price = price

car1 = Car("White")
car2 = Car("Red", 6, 20000)

print(car1.color)
print(car2.color)