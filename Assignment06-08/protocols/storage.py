from typing import Protocol, List, TypeVar, Type


class FileStorable(Protocol):
    ...

    @staticmethod
    def write_to_file(element: "FileStorable") -> List[str]:
        ...

    @staticmethod
    def read_from_file(*args) -> "FileStorable":
        ...
