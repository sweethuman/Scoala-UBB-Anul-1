"""
Problem 1 in the First Set
Generates the first prime number larger than a given natural number n
"""


def is_number_prime(number):
    """
    :param number: Number to be checked if it is prime
    :return: True if number prime, False if not
    """
    if number == 2:
        return True
    if number < 2:
        return False
    for j in range(2, number):
        if number % j == 0:
            return False
    return True


n = int(input('n = '))
i = n + 1

while not is_number_prime(i):
    i += 1

print("Largest number than", n, 'is', i)
