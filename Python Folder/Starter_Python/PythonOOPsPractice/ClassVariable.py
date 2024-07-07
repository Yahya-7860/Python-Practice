class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def CarName(self):
        return f"Car's brand is {self.brand} and model is {self.model}"


firstCar = Car('Mercedese', 'Benze')
print(firstCar.CarName())

secondCar = Car('Audi', 'Delux')
print(secondCar.CarName())
