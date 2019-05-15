class Dog:

    dogs = []

    def __init__(self, breed, colour):  #runs once
        self.breed = breed
        self.colour = colour
        # self.dogs.append(self)

    def bark(self):
        return "Woof"

    @classmethod
    def add(cls, dog):
        cls.dogs.append(dog)


fido = Dog('lab', 'black')
fido.bark()
Dog.add(fido)
