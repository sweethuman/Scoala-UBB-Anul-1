class Phone:
    def __init__(self, manufacturer: str, model: str, price: int):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__price = price

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __eq__(self, other):
        return self.price == other.price and self.manufacturer == other.manufacturer and self.model == other.model
