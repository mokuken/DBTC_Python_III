# Item 1
# Classify: Violates the Open-Closed Principle
# Justification: The original implementation uses conditional statements to determine the type of shape, 
# which makes it difficult to extend for new shapes without modifying the existing code.

# Refactored Design:
# The refactored code uses an abstract base class and polymorphism to allow for extension without modifying the existing code.
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, width, height, radius):
        self.width = width
        self.height = height
        self.radius = radius

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def calculate_area(radius):
        return 3.14 * radius ** 2

class Rectangle(Shape):
    def calculate_area(width, height):
        return width * height


# Item 2
# Classify: Follows the Open-Closed Principle
# Justification: The refactored code uses an abstract base class and ensures that each subclass implements the `send` method, 
# making it open for extension and closed for modification.

# Refactored Design:
# The refactored code ensures that each message type is handled by its own subclass, adhering to the OCP.
class Message(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailMessage(Message):
    def send(text):
        print(f"Sending Email: {text}")

class SMSMessage(Message):
    def send(text):
        print(f"Sending SMS: {text}")


# Item 3
# Classify: Violates the Open-Closed Principle
# Justification: The original implementation uses conditional statements to apply discounts, 
# which makes it difficult to add new discount types without modifying the existing code.

# Refactored Design:
# The refactored code uses an abstract base class and polymorphism to allow for extension without modifying the existing code.
from abc import ABC, abstractmethod

class Checkout(ABC):
    @abstractmethod
    def apply_discount(self):
        pass

class StudentDiscount(Checkout):
    def apply_discount(total_price):
        return total_price * 0.9

class SeniorDiscount(Checkout):
    def apply_discount(total_price):
        return total_price * 0.85


# Item 4
# Classify: Violates the Open-Closed Principle
# Justification: The original implementation has all report generation methods in a single class, 
# making it difficult to add new report types without modifying the existing code.

# Refactored Design:
# The refactored code uses an abstract base class and polymorphism to allow for extension without modifying the existing code.
from abc import ABC, abstractmethod

class Report:
    @abstractmethod
    def generate():
        pass

class GeneratePDF(Report):
    def generate():
        print("Generating PDF...")

class GenerateCSV(Report):
    def generate():
        print("Generating CSV...")

class GenerateHTML(Report):
    def generate():
        print("Generating HTML...")


# Item 5
# Classify: Adheres to the Open-Closed Principle
# Justification: The logger class is simple and does not require modification to add new functionality.

# Refactored Design:
# The refactored code removes unnecessary `self` usage, making the method static and easier to use.
class Logger:
    def log(message):
        print(f"[LOG] {message}")


# Test examples
# Item 1
print(Circle.calculate_area(5))
print(Rectangle.calculate_area(4, 4))

# Item 2
EmailMessage.send("This message is sent via email")
SMSMessage.send("This message is sent via sms")

# Item 3
print(StudentDiscount.apply_discount(45))
print(SeniorDiscount.apply_discount(45))

# Item 4
GeneratePDF.generate()
GenerateCSV.generate()
GenerateHTML.generate()

# Item 5
Logger.log("message")
