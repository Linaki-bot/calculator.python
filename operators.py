# Arithmetic Operators - Simple calculations

num1 = 56
num2 = 8

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2) # Modulus - Returns the remainder

# Comparison operatores - Compare values.
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2) # Equal to
print(num1 != num2) # Not equal to

# Assignment Operators = Assign values to variables
a = 200
print(a)

a += 20
print(a)

# Logic operators - and, or , not
x = 100
print(x < 250 and x > 1000)
print(x < 250 and x > 1000)
print( not(x < 250 and x > 1000))

# Operator predence - Order in which operations get executed.

output = (100-4 * 3 / 1)
print(int(output))

# Write a simple python program that returns the area of a trapezium

# A = 0.5 * (base1, base2, height)
def trapezium_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

# Test the function
def trapezium_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

base1 = 20
base2 = 14
height = 8

area = trapezium_area(base1, base2, height)
print(int(area))
