from abc import ABC, abstractmethod


class IHouseBuilder(ABC):
    """This Interface is for Builder"""

    @staticmethod
    @abstractmethod
    def set_building_type(building_type):
        pass

    @staticmethod
    @abstractmethod
    def set_doors(door_numbers):
        pass

    @staticmethod
    @abstractmethod
    def set_windows(window_numbers):
        pass

    @staticmethod
    @abstractmethod
    def set_house_material(house_material):
        pass

    @staticmethod
    @abstractmethod
    def get_house():
        pass
