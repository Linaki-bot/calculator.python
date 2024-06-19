class Car:
    def __init__(self, make, model, year):
        self.__make = make        # private attribute
        self.__model = model      # private attribute
        self.__year = year        # private attribute
        self.__mileage = 0       # private attribute, initialized to 0

    # getter method to access make attribute
    def get_make(self):
        return self.__make

    # setter method to update make attribute
    def set_make(self, make):
        self.__make = make

    # method to display car information
    def display_info(self):
        print(f"Car: {self.__year} {self.__make} {self.__model}, Mileage: {self.__mileage}")

    # method to update mileage
    def update_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            print("Mileage cannot be negative.")

# Creating an instance of Car
my_car = Car("Toyota", "Camry", 2020)

# Accessing and displaying car information using getter method
print("Make of the car:", my_car.get_make())

# Using setter method to update make
my_car.set_make("Honda")

# Displaying updated information
my_car.display_info()

# Trying to update mileage directly (which should be encapsulated)
my_car.__mileage = -10000  # This won't update the actual mileage due to encapsulation

# Updating mileage using the method provided
my_car.update_mileage(5000)
my_car.display_info()
