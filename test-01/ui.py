from phone import Phone
import services


def print_menu():
    print('')
    print('1. Add a phone\n'
          '2. Remove a phone\n'
          '3. Increase the price\n'
          '4. Show the list of phones, sorted by increasing price\n'
          '5. Exit')


def read_option(phone_list):
    while True:
        print_menu()
        read_value = input('Choose an option: ')
        print('')
        if read_value == '1':
            phone = read_phone()
            services.add_phone(phone_list, phone)
        elif read_value == '2':
            data = read_identifying_data()
            if services.remove_phone(phone_list, data[0], data[1]) is False:
                print('Sorry, the phone you entered does not exist in this shop')
        elif read_value == '3':
            phone = read_increase_price()
            if services.increase_price(phone_list, phone.manufacturer, phone.model, phone.price) is False:
                print('Sorry, the phone you entered does not exist in this shop')
        elif read_value == '4':
            print_phone_list(services.phones_ordered_by_price(phone_list))
        elif read_value == '5':
            break


def print_phone_list(phone_list):
    for phone in phone_list:
        print(phone.manufacturer, phone.model, phone.price)
    print('')


def read_phone():
    while True:
        manufacturer = input('Phone Manufacturer: ')
        model = input('Phone Model: ')
        price = input('Phone Price: ')
        if len(manufacturer) < 3 or len(model) < 3 or len(price) < 3:
            print('One of the fields has less than three characters')
            continue
        try:
            price = int(price)
        except ValueError:
            print('Price is not a number')
            continue
        return Phone(manufacturer, model, price)


def read_increase_price():
    while True:
        manufacturer = input('Phone Manufacturer: ')
        model = input('Phone Model: ')
        price = input('Amount to increase phone price by: ')
        try:
            price = int(price)
        except ValueError:
            print('Price is not a number')
            continue
        return Phone(manufacturer, model, price)


def read_identifying_data():
    while True:
        manufacturer = input('Phone Manufacturer: ')
        model = input('Phone Model: ')
        if len(manufacturer) < 3 or len(model) < 3:
            print('One of the fields has less than three characters')
            continue
        return manufacturer, model
