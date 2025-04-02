class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self._age = age     # protected attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
