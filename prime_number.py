"""Function to check if given number is a prime number or not"""


def prime_checker(number):
    for x in range(2, number-1):
        if number % x == 0:
            return "It's not a prime number."
    else:
        return "It's a prime number."


n = int(input("Check this number: "))
print(prime_checker(number=n))
