from abc import ABC, abstractmethod


class Component(ABC):
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """

    @abstractmethod
    def operation(self) -> str:
        pass
