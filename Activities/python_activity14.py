# Encapsulation
class UserProfile:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # private attribute

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password changed successfully.\n")
        else:
            print("Old password is incorrect.\n")

# Inheritance
class SmartDevice:
    def __init__(self, brand, status):
        self.brand = brand
        self.status = status

    def on(self):
        self.status = "on"
        print(f"{self.brand} is now on")

    def off(self):
        self.status = "off"
        print(f"{self.brand} is now off")

class SmartLight(SmartDevice):
    def adjust_brightness(self, level):
        print(f"Brightness adjusted to {level}%\n")

class SmartThermostat(SmartDevice):
    def set_temperature(self, temperature):
        print(f"Temperature set to {temperature}°C\n")

# Polymorphism
class PaymentMethod:
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₱{amount} using Credit Card.\n")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₱{amount} using PayPal.\n")

# Abstraction
from abc import ABC, abstractmethod

class ImageRecognitionModel(ABC):
    @abstractmethod
    def analyze_image(self, image):
        pass

class FaceRecognition(ImageRecognitionModel):
    def analyze_image(self, image):
        print(f"Analyzing image for faces: {image}")
        return "Face detected"

class ObjectRecognition(ImageRecognitionModel):
    def analyze_image(self, image):
        print(f"Analyzing image for objects: {image}")
        return "Object detected"

# Run test cases
# Encapsulation example usage
user = UserProfile(username="john_doe", password="old_password")
old_pass = input("\nEnter your old password: ")
new_pass = input("Enter your new password: ")
user.change_password(old_pass, new_pass)

# Inheritance example usage
device_type = input("\nSelect device to turn on (light/temp): ")

if device_type == "light":
    light = SmartLight(brand="Smart Light Device", status="off")
    light.on()
    brightness = int(input("Set brightness level (0-100): "))
    light.adjust_brightness(brightness)
elif device_type == "temp":
    thermostat = SmartThermostat(brand="Smart Thermostat Device", status="off")
    thermostat.on()
    temperature = int(input("Set temperature (°C): "))
    thermostat.set_temperature(temperature)
else:
    print("Invalid device selection.")

# Polymorphism example usage
def checkout(payment_method, amount):
    payment_method.pay(amount)

payment_choice = input("Choose payment method (credit/paypal): ").strip().lower()
amount = float(input("Enter the amount to pay: "))

if payment_choice == "credit":
    payment_method = CreditCard()
elif payment_choice == "paypal":
    payment_method = PayPal()
else:
    print("Invalid payment method.")
    payment_method = None

if payment_method:
    checkout(payment_method, amount)

# Abstraction example usage
face_recognition = FaceRecognition()
print(face_recognition.analyze_image("Image with someone's face"))

object_recognition = ObjectRecognition()
print(object_recognition.analyze_image("Theres a ball on image"))