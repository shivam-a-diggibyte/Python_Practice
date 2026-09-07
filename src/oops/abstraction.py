class CoffeeMachine:
    def make_coffee(self):
        self._boil_water()
        self._brew()
        print("Coffee is ready!")

    def _boil_water(self):
        print("Boiling water...")

    def _brew(self):
        print("Brewing coffee...")

machine = CoffeeMachine()
machine.make_coffee()


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

animal1=Dog()
animal1.make_sound()
