from Exception.Exceptions import *


class Repo:
    def _init_(self):
        self.__items_dictionary = {}

    def get_element(self, id):
        try:
            return self.__items_dictionary[id]
        except KeyError:
            raise RepositoryError("ID not existent")

    def add_item(self, new_item):
        try:
            if new_item.id in self.__items_dictionary.keys():
                raise RepositoryError("Id already exists!")
            self.__items_dictionary[new_item.id] = new_item
        except AttributeError:
            raise RepositoryError("Element does not have an id introduced!")

    def remove_item(self, id):
        try:
            if id in self.__items_dictionary.keys():
                del self.__items_dictionary[id]
            else:
                raise RepositoryError("Element does not exist!")
        except KeyError:
            raise RepositoryError("Element with that id does not exist!")

    def update_item(self, id, attribute, new_value):
        if id in self.__items_dictionary.keys():
            if hasattr(self.__items_dictionary[id], attribute):
                setattr(self.__items_dictionary[id], attribute, new_value)
            else:
                raise RepositoryError("Element with that id does not exist!")
        else:
            raise RepositoryError("Element with that id does not exist!")

    def search_item(self, attribute, search_value):
        searched_items = []
        try:
            if attribute == "id":
                search_value = int(search_value)
                if search_value in self.__items_dictionary.keys():
                    searched_items.append(self.__items_dictionary[search_value])
                else:
                    search_value = search_value.lower()
                    for item in self.__items_dictionary:
                        item_string = self.__items_dictionary[item].get_attribute_value(attribute).lower()
                        if item_string == search_value.lower() or item_string.find(search_value) != -1:
                            searched_items.append(self.__items_dictionary[item])
                return searched_items
        except ValueError as ve:
            raise RepositoryError(ve)

    @property
    def get_all(self):
        return self.__items_dictionary
