from complex import Complex
import re


def print_menu():
    print('1. Read Complex Number and Add it to List')
    print('2. Display entire list of Complex Numbers')
    print('3. Display on the console the longest sequence of distinct numbers. p6')
    print('4. Display on the console the longest sequence of numbers with a strictly increasing real part. p1')
    print('5. Exit')


def print_complex_numbers(complex_numbers):
    for c in complex_numbers:
        printalicious = '{} + {}i'.format(c.real, c.imaginary)
        print(printalicious)


def distinct_numbers(complex_numbers):
    """
    Calculates the longest sequence of distinct numbers and prints it
    :param complex_numbers: List of Complex Numbers
    :return: None
    """
    maxi_start = 0  # start position for the sequence of maximum length
    maxi_len = 0  # maximum length
    for i in range(0, len(complex_numbers) - 1):
        for j in range(i + 1, len(complex_numbers)):  # generates all the possible sequences
            ok = True
            for c in complex_numbers[i:j]:
                if complex_numbers[i:j].count(c) > 1:  # checks if a complex number is unique in the sequence
                    ok = False
            if ok is True and j - i > maxi_len:
                """
                if all complex numbers are unique and the sequence length is greater
                than the previuous one, it is saved
                """
                maxi_len = j - i
                maxi_start = i
    print_complex_numbers(complex_numbers[maxi_start: maxi_start + maxi_len])


def strictly_increasing(complex_numbers):
    """
    Calculates the longest sequence of numbers with a strictly increasing real part and prints it
    :param complex_numbers: List of Complex Numbers
    :return: None
    """
    maxi_start = 0  # start position for the sequence of maximum length
    maxi_len = 0  # maximum length
    current_start = 0  # start point for the sequence of current length
    current_len = 1  # current length
    for i in range(0, len(complex_numbers) - 1):
        if complex_numbers[i].real < complex_numbers[i + 1].real:  # checks if the next number is strictly increasing
            current_len += 1
        else:
            if current_len > maxi_len:
                maxi_len = current_len
                maxi_start = current_start
            current_start = i + 1
            current_len = 1
    if current_len > maxi_len:
        maxi_len = current_len
        maxi_start = current_start
    print_complex_numbers(complex_numbers[maxi_start: maxi_start + maxi_len])


def menu():
    complex_numbers = [Complex(7, 3), Complex(5, 6), Complex(7, 3), Complex(8, 4), Complex(9, 10), Complex(7, 3),
                       Complex(7, 3), Complex(7, 3), Complex(1, 3), Complex(2, 6), Complex(2, 6), Complex(0, 0),
                       Complex(1, 0), Complex(2, 0), Complex(3, 0), Complex(4, 0), Complex(5, 0)]
    while True:
        print_menu()
        read_option = input('>')
        if read_option == '1':
            complex_numbers.append(read_number())
        elif read_option == '2':
            print('Here is the complete list of complex numbers that have been entered:')
            print_complex_numbers(complex_numbers)
        elif read_option == '3':
            distinct_numbers(complex_numbers)
        elif read_option == '4':
            strictly_increasing(complex_numbers)
        elif read_option == '5':
            print('Exiting...')
            break
        else:
            print('This Option does not exist. Please select one from the menu')
        print('')


def read_number():
    while True:
        inputted = input("Enter Complex Number of form 'a + bi':")
        arr = inputted.split('+')
        arr[:] = [s.strip() for s in arr]  # strips splitted strings of whitespaces
        # checks using regex if the entered strings respect the complex number format of a + bi
        if re.fullmatch('^[+-]?([0-9]*[.])?[0-9]+$', arr[0]) is None:
            print('The Number you entered is not a Complex Number! Please try again...')
            continue
        else:
            real = float(arr[0])
        if re.fullmatch('^[+-]?([0-9]*[.])?[0-9]+i$', arr[1]) is None:
            print('The Number you entered is not a Complex Number! Please try again...')
            continue
        else:
            imaginary = float(arr[1].strip('i'))
        return Complex(real, imaginary)


def start():
    menu()


start()
