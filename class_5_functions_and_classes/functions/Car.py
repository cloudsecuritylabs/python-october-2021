class Car:
    def __init__(self, color, windows_number, price):
        self.color = color
        self.windows_number = windows_number
        self.price = price


blue_car = Car("Blue" , 4, 10000)
red_car = Car("Red", 6, 60000)

print(blue_car.price)
print(red_car.price)

print(blue_car.color)
print(blue_car.windows_number)

print(type(blue_car))
print(type(red_car))

