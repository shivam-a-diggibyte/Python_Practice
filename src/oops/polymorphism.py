class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("cat meows")

Animal=[Dog(),Cat()]

for i in Animal:
    i.sound()