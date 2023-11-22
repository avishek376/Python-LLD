from abc import abstractmethod, ABC


class IHouseBuilder(ABC):
    """
    Interface representation of House Builder Design Pattern
    """

    @staticmethod
    @abstractmethod
    def building_type(building_type):
        """Set building type"""

    @staticmethod
    @abstractmethod
    def wall_material(wall_material):
        """Set wall material"""

    @staticmethod
    @abstractmethod
    def no_of_doors(no_of_doors):
        """set no of doors"""

    @staticmethod
    @abstractmethod
    def no_of_windows(no_of_windows):
        """
        set no of windows
        """

    @staticmethod
    @abstractmethod
    def get_house():
        """
        get the house implementation
        """
