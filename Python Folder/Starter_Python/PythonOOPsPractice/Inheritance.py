class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def CarName(self):
        return f"Car's brand is {self.brand} and model is {self.model}"


class Electric_car(Car):
    def __init__(self, brand, model, size):
        super().__init__(brand, model)
        self.battery_size = size
    
    def ElectricCarName(self):
        return f"Car's brand is {self.brand} and model is {self.model} and battery is {self.battery_size}"


firstElectricCar = Electric_car('Mercedese', 'Benze', '800mm')
print(firstElectricCar.brand)
print(firstElectricCar.model)
print(firstElectricCar.battery_size)
print(firstElectricCar.ElectricCarName())

# firstCar = Car('Mercedese', 'Benze')
# secondCar = Car('Audi', 'Delux')
# print(secondCar.CarName())
