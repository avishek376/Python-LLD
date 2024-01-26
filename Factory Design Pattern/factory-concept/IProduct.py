from abc import ABC, abstractmethod


class IProduct(ABC):
    """This interface is common for all instances"""

    @abstractmethod
    def description(self):
        """Implemented class will provide their own descriptions"""
        pass

