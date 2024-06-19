
class Car:
    def __init__(self, model, color, manufacturer, yof,):
        self.model = model
        self.color = color
        self.manufacturer = manufacturer
        self.yof = yof


    def speed(self):
        print(self.model,"is moving at ",self.speed,"km/hr")

car1 = Car("B12", "white", "BMW", 2024)

car2 = Car("B12", "blue", "BMW", 2020)
car3 = Car("B12", "black", "BMW", 2014)
car4 = Car("B12", "red", "BMW", 2012)
