from typing import List

from phone import Phone


def add_phone(phone_list: List[Phone], phone: Phone):
    """
    Adds a phone to the list
    @param phone_list: The List of phones to add to
    @param phone: The Phone to add
    """
    phone_list.append(phone)


def remove_phone(phone_list: List[Phone], manufacturer, model):
    """
    Removes a phone from the list using manufacturer and model as identifier
    @param phone_list: The Phone List to remove from
    @param manufacturer: The Manufacturer of the Phone
    @param model: The Model of the Phone
    @return: True if it is successful, False if the phone with the identifiers was not found
    """
    index = search_phone(phone_list, manufacturer, model)
    if index is False:
        return index
    phone_list.pop(index)
    return True


# should it add over the price or just set it?
def increase_price(phone_list: List[Phone], manufacturer: str, model: str, price: int):
    """
    Increases the price of a phone by a given amount, find it using manufacturer and model as identifiers
    @param phone_list: Phone list where to find the phone
    @param manufacturer: The Manufacturer of the Phone
    @param model: The Model of the Phone
    @param price: The Amount to increase the price by
    @return: True if it is successful, False if the phone with the identifiers was not found
    """
    index = search_phone(phone_list, manufacturer, model)
    if index is False:
        return index
    phone_list[index].price += price
    return True


def phones_ordered_by_price(phone_list: List[Phone]):
    """
    Orders the phones in the phones list ascending according to price
    @param phone_list: The Phone List to Sort
    @return: The Sorted phone List
    """
    return sorted(phone_list, key=lambda x: x.price)


def search_phone(phone_list: List[Phone], manufacturer, model):
    """
    Searches for the phone in the list using the manufacturer and model as identifiers
    @param phone_list: The Phone list to search in
    @param manufacturer: The Manufacturer of the Phone
    @param model: The Model of the Phone
    @return: The Index of the phone in the list if it is found, False if it is not found
    """
    for i in range(len(phone_list)):
        if phone_list[i].manufacturer == manufacturer and phone_list[i].model == model:
            return i
    return False
