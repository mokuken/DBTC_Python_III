from abc import ABC, abstractmethod

class PowerControl(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class TempControl(ABC):
    @abstractmethod
    def set_temperature(self, temp):
        pass

class WashControl(ABC):
    @abstractmethod
    def start_wash_cycle(self):
        pass

class ChannelControl(ABC):
    @abstractmethod
    def change_channel(self, channel):
        pass
    

class SmartTV(PowerControl, ChannelControl):
    def turn_on(self):
        print("TV is now ON")

    def turn_off(self):
        print("TV is now OFF")

    def change_channel(self, channel):
        print(f"Changing channel to {channel}")

class SmartFridge(PowerControl, TempControl):
    def turn_on(self):
        print("Fridge is now ON")

    def turn_off(self):
        print("Fridge is now OFF")

    def set_temperature(self, temp):
        print(f"Fridge temperature set to {temp}°C")

class SmartWasher(PowerControl, WashControl):
    def turn_on(self):
        print("Washer is now ON")

    def turn_off(self):
        print("Washer is now OFF")

    def start_wash_cycle(self):
        print("Wash cycle started")

class SmartOven(PowerControl, TempControl):
    def turn_on(self):
        print("Oven is now ON")

    def turn_off(self):
        print("Oven is now OFF")

    def set_temperature(self, temp):
        print(f"Oven temperature set to {temp}°C")


o = SmartOven()
o.turn_on()
o.set_temperature(60)
o.turn_off()