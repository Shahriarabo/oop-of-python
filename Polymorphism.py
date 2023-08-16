class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


# inherit from vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')


# Car Object
car = Car('Car x1', 'Red', 20000)
car.show()
# calls methods from Car class
car.max_speed()
car.change_gear()

# Vehicle Object
vehicle = Vehicle('Truck x1', 'white', 75000)
vehicle.show()
# calls method from a Vehicle class
vehicle.max_speed()
vehicle.change_gear()

class cars:
    def __init__(self, name, Brand, Color, Country):
        self.name = name
        self.Brand = Brand
        self.Color = Color
        self.Country = Country

class car(cars):
    pass
class car1(cars):
    pass
p= car("FLy","BMW","Black","Bd")
c =  car("FLy","bstr","Black","Bd")

print("Car name is ",p.name,)
print("Car Branfd is ",p.Brand)
print("Car color is ",p.Color)
print("Country name is ",p.Country)


print("Car name is ",c.name,)
print("Car Branfd is ",c.Brand)
print("Car color is ",c.Color)
print("Country name is ",c.Country)