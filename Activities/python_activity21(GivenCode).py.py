# 2. Analyze the Problem:
#     ◦ Why is this code violating the Interface Segregation Principle?
#       ans: it violates the ISP because it forced to use an interface that doesnt use on specific device

#     ◦ Which classes are forced to implement methods they don’t use?
#       ans: the SmartTV, SmartFridge, SmartWasher it forced all the methods of an interface that unrelated to a device

#     ◦ What’s the problem with using raise NotImplementedError()?
#       ans: the problem is the child class is force to use the NotImplementedError() for a method that not related to the device
#            for example the tv it forced to use the set_temperature() method even the tv can't manually change the temp it self

from abc import ABC, abstractmethod

# Monolithic interface
class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def change_channel(self, channel):
        pass

    @abstractmethod
    def set_temperature(self, temp):
        pass

    @abstractmethod
    def start_wash_cycle(self):
        pass

class SmartTV(SmartDevice):
    def turn_on(self):
        print("TV is now ON")

    def turn_off(self):
        print("TV is now OFF")

    def change_channel(self, channel):
        print(f"Changing channel to {channel}")

    def set_temperature(self, temp):
        raise NotImplementedError("TV can't set temperature")

    def start_wash_cycle(self):
        raise NotImplementedError("TV can't wash clothes")

class SmartFridge(SmartDevice):
    def turn_on(self):
        print("Fridge is now ON")

    def turn_off(self):
        print("Fridge is now OFF")

    def change_channel(self, channel):
        raise NotImplementedError("Fridge can't change channels")

    def set_temperature(self, temp):
        print(f"Fridge temperature set to {temp}°C")

    def start_wash_cycle(self):
        raise NotImplementedError("Fridge can't wash clothes")

class SmartWasher(SmartDevice):
    def turn_on(self):
        print("Washer is now ON")

    def turn_off(self):
        print("Washer is now OFF")

    def change_channel(self, channel):
        raise NotImplementedError("Washer can't change channels")

    def set_temperature(self, temp):
        raise NotImplementedError("Washer doesn't control temperature like a fridge")

    def start_wash_cycle(self):
        print("Wash cycle started")