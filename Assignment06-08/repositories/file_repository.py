from typing import Type, Callable, TypeVar, List, Generic

from repositories.repository import Repository, KeyType
from protocols import FileStorable

RepoType = TypeVar("RepoType", bound=FileStorable)


class FileRepository(Repository, Generic[RepoType]):
    def __init__(
        self, repo_type: Type[RepoType], key_type: Type[KeyType], key: Callable[[RepoType], KeyType], file_name: str
    ):
        super().__init__(repo_type, key_type, key)
        self._file_name = file_name
        self.__load()

    def __load(self):
        with open(self._file_name) as file:
            for line in file:
                line = line.strip()
                args = line.split(",")
                element = self._repo_type.read_from_file(*args)
                super().add_element(element)

    def __write_to_file(self):
        with open(self._file_name, "w") as file:
            for element in self._items.values():
                args: List[str] = self._repo_type.write_to_file(element)
                line = ",".join(args)
                file.write(line)
                file.write("\n")

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
