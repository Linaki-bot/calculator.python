# Inbuilt functions/Standard library functions

y = min(23, 56, 1000, 5647)
print(y)

x = max(90, 2, 76, 14)
print("The maximum number is", x)

z = pow(2, 3)
print(z)

# User-defined functions
def school() :
    print("eMobilis")

school()  # Calling a function

def multiply():
    num1 = 5
    num2 = 6
    print(num1 * num2)
multiply()

# Parameters and arguments
def add(a, b):
    print(a + b)
add(5, 6)
add(10, 2)
add(56, 78)
add(90, 50)

def Employee(fullname, age, salary, phone, position):
    print(fullname, age, salary, phone, position)

Employee("Jason Shikuku", 45, 500000, 724466959, "MD")
Employee("Sharon Wangui", 30, 200000, 724456859, "Secretary")
Employee("David Kimani", 38, 450000, 724456859, "Project Manager")
Employee("Mercy Wanjiku", 36, 250000, 724456859, "Contractor")
Employee("Jahleel Kinyanjui", 29, 120000, 724456859, "Clerk")