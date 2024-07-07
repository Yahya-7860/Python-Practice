class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


FirstInstance = Car('Mercedece', 'Benze')
print(FirstInstance.brand)
print(FirstInstance.model)

SecondInstance = Car('Tata', 'Herrier')
print(SecondInstance.brand)
print(SecondInstance.model)
