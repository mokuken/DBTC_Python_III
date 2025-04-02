class Bird:
    def speak(self):
        print("Bird chirps")

class Dog:
    def speak(self):
        print("Dog barks")

animals = [Bird(), Dog()]
for animal in animals:
    animal.speak()  # Output: Bird chirps \n Dog barks
