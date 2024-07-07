class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def CarName(self):
        return f"Car's brand is {self.__brand} and model is {self.model}"

    def get_brand(self):
        return self.__brand


class Electric_car(Car):
    def __init__(self, brand, model, size):
        super().__init__(brand, model)
        self.battery_size = size

    def ElectricCarName(self):
        return f"Car's brand is {self.__brand} and model is {self.model} and battery is {self.battery_size}"


firstElectricCar = Electric_car('Mercedese', 'Benze', '800mm')
print(firstElectricCar.get_brand())
