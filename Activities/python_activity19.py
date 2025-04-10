# Original Code
class Car:
    def __init__(self, fuel: int):
        self.fuel = fuel

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 1
            print("Car is driving!")
        else:
            raise Exception("Not enough fuel to drive!")

    def refuel(self, amount: int):
        self.fuel += amount
        print(f"Car refueled by {amount}.")

# This violates the LSP because the ElectricCar class changes the behavior of the refuel method
# and introduces a new recharge method, which is not present in the base class.
# This makes it impossible to substitute an ElectricCar where a Car is expected.
class ElectricCar(Car):
    def __init__(self, battery: int):
        self.fuel = battery  # Incorrectly reusing 'fuel' for the battery
        self.battery = battery

    def drive(self):
        if self.battery > 0:
            self.battery -= 1
            print("Electric car is driving!")
        else:
            raise Exception("Not enough battery to drive!")

    def refuel(self, amount: int):
        raise NotImplementedError("Electric cars can't refuel with fuel!")  # Violates LSP

    def recharge(self, amount: int):
        self.battery += amount
        print(f"Electric car recharged by {amount}.")






# Refactored Code
from abc import ABC, abstractmethod

class Vehicle():
    @abstractmethod
    def drive(self):
        pass

class FuelVehicle(Vehicle):
    def __init__(self, fuel: int):
        self.fuel = fuel

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 1
            print("The fuel vehicle is driving!")
        else:
            raise Exception("Not enough fuel to drive!")
        
    def refuel(self, amount: int):
        self.fuel += amount
        print(f"Fuel vehicle refueled by {amount}.")

class ElectricVehicle(Vehicle):
    def __init__(self, battery: int):
        self.battery = battery

    def drive(self):
        if self.battery > 0:
            self.battery -= 1
            print("The electric vehicle is driving!")
        else:
            raise Exception("Not enough battery to drive!")
    
    def recharge(self, amount: int):
        self.battery += amount
        print(f"Electric vehicle recharged by {amount}.")


# Example usage of the refactored code

# Create a fuel vehicle
toyota = FuelVehicle(fuel=46)
toyota.drive()
toyota.refuel(15)

# Create an electric vehicle
tesla = ElectricVehicle(battery=78)
tesla.drive()
tesla.recharge(7)
