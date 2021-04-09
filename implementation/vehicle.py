from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass
    @abstractmethod
    def refuel(self):
        pass

class Car(Vehicle):
    def __init__(self,fuel_quantity,fuel_consumption):
        self.fuel_quantity=fuel_quantity
        self.fuel_consumption=fuel_consumption

    def setSummer(self):
        self.summer = True

    def drive(self, distance):
        if self.summer:
            self.fuel_consumption += 0.9
        fuel_consumed=self.fuel_consumption*distance
        self.fuel_quantity -= fuel_consumed

    def refuel(self, fuel_quantity):
        self.fuel_quantity += fuel_quantity
        

class Truck(Vehicle):
    def __init__(self,fuel_quantity,fuel_consumption):
        self.fuel_quantity=fuel_quantity
        self.fuel_consumption=fuel_consumption
    
    def setSummer(self):
        self.summer = True

    def drive(self, distance):
        if self.summer:
            self.fuel_consumption += 1.6
        fuel_consumed=self.fuel_consumption*distance
        self.fuel_quantity -= fuel_consumed

    def refuel(self, fuel_quantity):
        self.fuel_quantity += (95/100 * fuel_quantity)
        

car = Car(20, 5)
car.setSummer()
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


truck = Truck(100, 15)
truck.setSummer()
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)