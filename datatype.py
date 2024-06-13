# Datatype

number = 78  # Int
num = 45.09  # Float
greeting = "How are you doing"  # str
is_Programming_Interesting = True  #bool
devices = ["Laptop", "Computer", "Tablet", "Phone"] # List
browser = ("Opera", "Chrome", "Safari", "Brave") # Tuple
countries = {"United States", "India", "Japan", "Spain"} # Set
employee ={
    "firstname": "John",
    "age": 23,
    "nationality": "Kenyan",
    "emailaddress": "john@gmail.com",
} # Dictionary

print(is_Programming_Interesting)
print(devices)
print(browser)
print(countries)
print(num)
print(employee["firstname"])

# Determining a datatype
print(type(countries))
print(type(employee))

# Typecasting is the process of converting one data type to another
print(int(num))
print(float(number))
