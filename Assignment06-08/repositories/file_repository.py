from typing import Type, Callable, TypeVar, List

from repositories.repository import Repository, KeyType
from protocols import FileStorable

RepoType = TypeVar("RepoType", bound=FileStorable)


class FileRepository(Repository):
    def __init__(
        self, repo_type: Type[RepoType], key_type: Type[KeyType], key: Callable[[RepoType], KeyType], file_name: str
    ):
        super().__init__(repo_type, key_type, key)
        self.__file_name = file_name
        self.__load()

    def __load(self):
        with open(self.__file_name) as file:
            for line in file:
                args = line.split(",")
                element: FileStorable = self.__repo_type.read_from_file(*args)
                super().add_element(element)

    def __write_to_file(self):
        with open(self.__file_name, "w") as file:
            args: List[str] = self.__repo_type.write_to_file()
            line = ",".join(args)
            file.write(line)
            file.write("\n")

    def add_element(self, element: RepoType):
        pass

    def remove_element(self, key: KeyType) -> RepoType:
        pass

    def update_item(self, key: KeyType, attribute: str, value):
        pass
