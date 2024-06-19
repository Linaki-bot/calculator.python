
# Class is a blueprint of an object
# Object is an instance of a class

class Person:
    # Properties/Attributes/Variables/Characteristics
    name = "James"
    age = 23
    gender ="Male"

    # Methods/Function/Behaviour
    def move(self):
        print("Person is walking")

farmer = Person()
farmer.move()
print(farmer.name)
print(farmer.age)
print(farmer.gender)

Doctor = Person()