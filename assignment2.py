# A python programme to check whether a number is prime or odd
def is_prime(number):
    """ Function to check if a number is prime """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def is_odd(number):
    """ Function to check if a number is odd """
    return number % 2 != 0


def main():
    number = int(input("Enter a number: "))

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

    if is_odd(number):
        print(f"{number} is an odd number.")
    else:
        print(f"{number} is not an odd number.")


if __name__ == "__main__":
    main()
