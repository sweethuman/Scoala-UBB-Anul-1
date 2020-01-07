from typing import Generic, TypeVar, Dict, Callable, List

KeyType = TypeVar("KeyType")
DataType = TypeVar("DataType")


class Dictionary(Generic[KeyType, DataType]):
    def __init__(self):
        self.dict: Dict[KeyType, DataType] = {}

    def __getitem__(self, item: KeyType):
        return self.dict[item]

    def __setitem__(self, key: KeyType, value: DataType):
        self.dict[key] = value

    def __delitem__(self, key: KeyType):
        del self.dict[key]

    def __iter__(self):
        return DictionaryIterator(self)

    def __len__(self):
        return len(self.dict)

    def get(self, key: KeyType):
        return self.dict.get(key)

    def values(self):
        return self.dict.values()

    def pop(self, key: KeyType):
        return self.dict.pop(key)


class DictionaryIterator:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.pos = iter(self.dictionary.dict)

    def __next__(self):
        return next(self.pos)


def gnome_sort(obj: List[DataType], cmp: Callable[[DataType, DataType], bool]):
    i = 0
    while i < len(obj):
        if i == 0:
            i += 1
        if cmp(obj[i], obj[i - 1]):
            obj[i - 1], obj[i] = obj[i], obj[i - 1]
            i -= 1
        else:
            i += 1


def my_filter(obj: List[DataType], acceptable: Callable[[DataType], bool]):
    new_list = []
    for i in obj:
        if acceptable(i):
            new_list.append(i)
    return new_list


# def some_func(x: int, y: int):
#     if x < y:
#         return True
#     return False
#
#
# listing = [0, 3, 7, 5, 3, 2, 1]
# stupid_sort(listing, some_func)
# print(listing)
