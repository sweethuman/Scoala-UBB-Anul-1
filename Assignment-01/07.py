"""
Problem 7 in Second Set
Determines the twin prime numbers p1 and p2 immediately larger than the given non-null
natural number n
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
p1 = n + 1
if p1 % 2 == 0:
    p1 += 1
p2 = p1 + 2

while not is_number_prime(p1) or not is_number_prime(p2):
    p1 += 2
    p2 += 2

print("Twin primes:", p1, p2)
