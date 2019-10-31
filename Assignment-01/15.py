"""
Problem 15 in Third Set
"""


def get_divisors(number):
    """
    :param number: Number for which to return list of divisors
    :return: List of Divisors for the given number
    """
    divisors = []
    for j in range(1, number):
        if number % j == 0:
            divisors.append(j)
    return divisors


def get_solution(number):
    """
    Calculates the largest perfect number smaller than a given natural number n.
    :param number: Number for which to calculate the solution of the problem
    :return: Number if solution exists, otherwise None
    """
    for i in range(number - 1, -1, -1):
        divisors = get_divisors(i)
        sumix = 0
        for j in divisors:
            sumix += j
        if sumix == i and len(divisors) is not 0:
            return i
    return None


n = int(input('n = '))

solution = get_solution(n)
if solution is not None:
    print("The largest perfect number smaller than", n, 'is', solution)
else:
    print("There is no largest perfect number smaller than", n)
