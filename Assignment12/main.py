from typing import List
import copy

posibilities = [1, 2, 5]


def calculate_coin_payment(sumix: int, options: List[int], combination: List[int], current_pos):
    if sum(combination) == sumix:
        print(combination)
    elif sum(combination) > sumix:
        return
    for i in range(current_pos, len(options)):
        combination.append(options[i])
        calculate_coin_payment(sumix, options, combination, i)
        combination.pop()


calculate_coin_payment(11, posibilities, [], 0)
print('')
stack = [[[], 0]]


def calculate_coin_payment_iteratively(sumix: int, options: List[int]):
    while len(stack) != 0:
        current = stack.pop()
        for i in range(current[1], len(options)):
            combination = copy.copy(current[0])
            combination.append(options[i])
            if sum(combination) == sumix:
                print(combination)
                continue
            elif sum(combination) > sumix:
                continue
            stack.append([combination, i])


calculate_coin_payment_iteratively(11, posibilities)
