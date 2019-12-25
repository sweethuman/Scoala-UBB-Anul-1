from typing import Type, Callable, TypeVar, List, Generic

from repositories.repository import Repository, KeyType
from protocols import FileStorable
import pickle
import os

RepoType = TypeVar("RepoType", bound=FileStorable)


class PickleRepository(Repository, Generic[RepoType]):
    def __init__(
        self, repo_type: Type[RepoType], key_type: Type[KeyType], key: Callable[[RepoType], KeyType], file_name: str
    ):
        super().__init__(repo_type, key_type, key)
        self._file_name = file_name
        self.__load()

    def __load(self):
        if (
            not os.path.exists(os.getcwd() + "/" + self._file_name)
            or os.path.getsize(os.getcwd() + "/" + self._file_name) == 0
        ):
            return
        with open(self._file_name, "rb") as file:
            self._items = pickle.load(file)

    def __write_to_file(self):
        with open(self._file_name, "wb") as file:
            pickle.dump(self._items, file)

    def add_element(self, element: RepoType):
        super().add_element(element)
        self.__write_to_file()

    def remove_element(self, key: KeyType) -> RepoType:
        element = super().remove_element(key)
        self.__write_to_file()
        return element

    def update_item(self, key: KeyType, attribute: str, value):
        super().update_item(key, attribute, value)
        self.__write_to_file()
