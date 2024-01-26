from abc import ABC, abstractmethod


class Burger(ABC):
    """Abstract class for Burger"""

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass
