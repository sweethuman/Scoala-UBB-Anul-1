from errors import RepositoryError
from typing import Callable, TypeVar, Dict, Type, Generic, Hashable, Union, List

RepoType = TypeVar("RepoType")
KeyType = TypeVar("KeyType", bound=Union[int, str, tuple, Hashable])


class Repository(Generic[RepoType, KeyType]):
    def __init__(self, repo_type: Type[RepoType], key_type: Type[KeyType], key: Callable[[RepoType], KeyType]):
        self.__items: Dict[KeyType, RepoType] = {}
        self.__key = key
        self.__repo_type = repo_type
        self.__key_type = key_type

    def get_element(self, key: KeyType) -> RepoType:
        if self.__items.get(key):
            return self.__items[key]
        raise RepositoryError("Element with given key doesn't exist")

    def exists_element(self, key: KeyType) -> bool:
        if self.__items.get(key):
            return True
        else:
            return False

    def add_element(self, element: RepoType):
        self.__items[self.__key(element)] = element

    def remove_element(self, key: KeyType) -> RepoType:
        if self.__items.get(key):
            return self.__items.pop(key)
        else:
            raise RepositoryError("Element with given key doesn't exist")

    def update_item(self, key: KeyType, attribute: str, value):
        if self.__items.get(key):
            if hasattr(self.__items[key], attribute):
                setattr(self.__items[key], attribute, value)
            else:
                raise RepositoryError("Element doesn't have given attribute")
        else:
            raise RepositoryError("Element with given key doesn't exist")

    def search_items(self, attribute: str, value) -> List[RepoType]:
        result_items: List[RepoType] = []
        for item in self.__items.values():
            if hasattr(item, attribute) and getattr(item, attribute) == value:
                result_items.append(item)
        return result_items

    @property
    def get_all(self) -> List[RepoType]:
        return list(self.__items.values())
