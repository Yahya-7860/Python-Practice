class Car:
    count = 0

    def __init__(self, brand, model):
        Car.count += 1
        self.__brand = brand
        self.model = model

    def CarName(self):
        return f"Car's brand is {self.__brand} and model is {self.model}"

    def get_brand(self):
        return self.__brand

    def fuel_type(self):
        return 'Petorl and Diseal'


class Electric_car(Car):
    def __init__(self, brand, model, size):
        super().__init__(brand, model)
        self.battery_size = size

    def ElectricCarName(self):
        return f"Car's brand is {self.__brand} and model is {self.model} and battery is {self.battery_size}"

    def fuel_type(self):
        return 'Battery and Charging'


firstCar = Car("Tata", "Safari")
secondCar = Car("Tata", "Safari")
print(f"{firstCar.count} objects created")
# print(f"{Car.count} objects created")
