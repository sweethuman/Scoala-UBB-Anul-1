import services
from phone import Phone


def test_add_phone():
    phone_list = []
    services.add_phone(phone_list, Phone('Lamba', 'The One', 50634))
    assert phone_list[0] == Phone('Lamba', 'The One', 50634)


def test_remove_phone():
    phone_list = [Phone('Lamba', 'The One', 50634), Phone('Lamba', 'The Two', 50634)]
    assert services.remove_phone(phone_list, 'Lamba', 'The One') is True
    assert phone_list[0] == Phone('Lamba', 'The Two', 50634)
    assert services.remove_phone(phone_list, 'Lamba', 'The One') is False


def test_increase_price():
    phone_list = [Phone('Lamba', 'The One', 50634)]
    assert services.increase_price(phone_list, 'Lamba', 'The One', 100) is True
    assert phone_list[0] == Phone('Lamba', 'The One', 50734)
    assert services.increase_price(phone_list, 'Lamba', 'The Three', 100) is False


def test_phones_ordered_by_price():
    phone_list = [Phone('Lamba', 'The One', 5634), Phone('Lamba', 'The Two', 634)]
    ordered_list = services.phones_ordered_by_price(phone_list)
    assert ordered_list[0] == Phone('Lamba', 'The Two', 634) and ordered_list[1] == Phone('Lamba', 'The One', 5634)


def test_search_phone():
    phone_list = [Phone('Lamba', 'The One', 50634), Phone('Lamba', 'The Two', 50634),
                  Phone('Lamba', 'The Three', 50634)]
    index = services.search_phone(phone_list, 'Lamba', 'The Two')
    assert index == 1
    index = services.search_phone(phone_list, 'Lamba', 'The Ciao')
    assert index is False


def run_all_tests():
    test_add_phone()
    test_remove_phone()
    test_increase_price()
    test_phones_ordered_by_price()
    test_search_phone()
