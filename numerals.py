def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example usage:
num1 = 10
num2 = 20
num3 = 15

largest = find_largest(num1, num2, num3)
print("The largest number among", num1, ",", num2, ", and", num3, "is:", largest)

first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
third = int(input("Enter third number : "))
fourth = int(input("Enter fourth number : "))

if first < second and first < third and first < fourth :
    print(first, "is the smallest number")
elif second <first and second < third and second < fourth :
    print(second, "is the smallest number")
elif third <first and third < second and third < fourth :
    print(third,"is the smallest number")
else:
    print(fourth, "is the smallest number")

# A simple calculator program
