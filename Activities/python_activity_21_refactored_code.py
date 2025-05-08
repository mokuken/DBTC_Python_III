"""Module providing a function abstraction"""

from abc import ABC, abstractmethod


class PowerControl(ABC):
    """Class representing a smart device"""
    @abstractmethod
    def turn_on(self):
        """Function for turning on power"""

    @abstractmethod
    def turn_off(self):
        """Function for turning off power"""

    def is_on(self):
        """Check if the device is on"""
        print("Checking if the device is ON")


class TempControl(ABC):
    """Class representing a controller for temperature"""
    @abstractmethod
    def set_temperature(self, temp):
        """Function for changing temperature"""

    def get_temperature(self):
        """Get the current temperature"""
        print("Getting the current temperature")


class WashControl(ABC):
    """Class representing a controller for washing machine"""
    @abstractmethod
    def start_wash_cycle(self):
        """Function for starting the washing cycle"""

    def stop_wash_cycle(self):
        """Function for stopping the washing cycle"""
        print("Stopping the wash cycle")


class ChannelControl(ABC):
    """Class representing a controller for changing channel"""
    @abstractmethod
    def change_channel(self, channel):
        """Function for changing the channel"""

    def get_current_channel(self):
        """Get the current channel"""
        print("Getting the current channel")


class SmartTV(PowerControl, ChannelControl):
    """Class representing a smart television"""
    def turn_on(self):
        print("TV is now ON")

    def turn_off(self):
        print("TV is now OFF")

    def change_channel(self, channel):
        print(f"Changing channel to {channel}")

    def get_current_channel(self):
        print("Current channel is 101")


class SmartFridge(PowerControl, TempControl):
    """Class representing a smart refrigerator"""
    def turn_on(self):
        print("Fridge is now ON")

    def turn_off(self):
        print("Fridge is now OFF")

    def set_temperature(self, temp):
        print(f"Fridge temperature set to {temp}°C")

    def get_temperature(self):
        print("Current fridge temperature is 4°C")


class SmartWasher(PowerControl, WashControl):
    """Class representing a smart washing machine"""
    def turn_on(self):
        print("Washer is now ON")

    def turn_off(self):
        print("Washer is now OFF")

    def start_wash_cycle(self):
        print("Wash cycle started")

    def stop_wash_cycle(self):
        print("Wash cycle stopped")


class SmartOven(PowerControl, TempControl):
    """Class representing a smart oven"""
    def turn_on(self):
        print("Oven is now ON")

    def turn_off(self):
        print("Oven is now OFF")

    def set_temperature(self, temp):
        print(f"Oven temperature set to {temp}°C")

    def get_temperature(self):
        print("Current oven temperature is 180°C")


o = SmartOven()
o.turn_on()
o.set_temperature(60)
o.get_temperature()
o.turn_off()
