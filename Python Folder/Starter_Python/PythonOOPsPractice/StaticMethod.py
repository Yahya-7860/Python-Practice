class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    @staticmethod
    def generalInfo():
        return 'Car is Mean of transport'

    @property
    def getBrand(self):
        return self.__brand


myCar = Car('hero', 'heroin')
# print(Car.generalInfo())
print(myCar.getBrand)