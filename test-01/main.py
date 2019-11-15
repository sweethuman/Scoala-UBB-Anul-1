from ui import read_option
from phone import Phone
from tests import run_all_tests


def main():
    run_all_tests()
    phone_list = [Phone('Samsung', 'Note 10', 3000), Phone('Samsung', 'Note 9', 2000),
                  Phone('Samsung', 'Note 17', 6000), Phone('Motorola', 'Moto GO', 600),
                  Phone('Huawi', 'P20', 1000)]
    read_option(phone_list)


main()
