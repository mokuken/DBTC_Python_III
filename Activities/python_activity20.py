class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method!")

    def get_energy_level(self):
        raise NotImplementedError("Subclasses must implement this method!")

    def perform_action(self):
        raise NotImplementedError("Subclasses must implement this method!")


class Dog(Animal):
    def __init__(self):
        self.energy = 100

    def make_sound(self):
        print("Woof!")

    def get_energy_level(self):
        return self.energy

    def perform_action(self):
        print("Dog is running!")
        self.energy = self.energy - 20


class Cat(Animal):
    def __init__(self):
        self.energy = 90

    def make_sound(self):
        print("Meow!")

    def get_energy_level(self):
        return self.energy

    def perform_action(self):
        print("Cat is purring and stretching!")
        self.energy = self.energy - 10


class RobotDog(Animal):
    def __init__(self):
        self.energy = 100

    def make_sound(self):
        print("Beep-Bop!")

    def get_energy_level(self):
        return self.energy

    def perform_action(self):
        if self.energy < 10:
            print("RobotDog is recharging...")
            self.charge_battery()
        else:
            print("RobotDog is patrolling!")
            self.energy -= 10

    def charge_battery(self):
        print("Charging complete.")
        self.energy = 100


class RobotCat(Animal):
    def __init__(self):
        self.energy = 100

    def make_sound(self):
        print("Meow... Beep!")

    def get_energy_level(self):
        return self.energy

    def perform_action(self):
        if self.energy < 10:
            print("RobotCat is low on power. Recharging...")
            self.charge_battery()
        else:
            print("RobotCat is scanning the environment!")
            self.energy -= 5

    def charge_battery(self):
        print("RobotCat fully recharged.")
        self.energy = 100


# ---------- LISKOV TEST FUNCTION ---------- #
def perform_sound_and_action(animal: Animal):
    animal.make_sound()
    animal.perform_action()
    print(f"Energy Level: {animal.get_energy_level()}")


# ---------- TEST CASES ---------- #
dog = Dog()
cat = Cat()
robot_dog = RobotDog()
robot_cat = RobotCat()

print("\nDog:")
perform_sound_and_action(dog)
perform_sound_and_action(dog)
print("\nCat:")
perform_sound_and_action(cat)
print("\nRobot Dog:")
perform_sound_and_action(robot_dog)
print("\nRobot Cat:")
perform_sound_and_action(robot_cat)