from abc import ABC, abstractmethod


class NavigationStrategy(ABC):
    """This interface represents the Navigation Strategy"""

    @abstractmethod
    def navigate(self, source, destination):
        pass
