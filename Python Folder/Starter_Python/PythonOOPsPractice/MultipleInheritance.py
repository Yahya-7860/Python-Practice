class Battery():
    def btry(self):
        return 'i am battery'


class Engine():
    def eng(self):
        return 'i am engine'


class Two_Inherited_Electric_Car(Battery, Engine):
    pass


TwoCar = Two_Inherited_Electric_Car()
print(TwoCar.btry())
print(TwoCar.eng())
