from House import *
from IHouseBuilder import *


class HouseBuilder(IHouseBuilder):
    """This class implements IBuilder interface"""

    def __init__(self):
        self.house_builder = House()

    def set_house_material(self, house_material):
        self.house_builder.house_material = house_material
        return self

    def set_building_type(self, building_type):
        self.house_builder.building_type = building_type
        return self

    def set_doors(self, door_numbers):
        if type(door_numbers) != int:
            raise AttributeError("Pass numerical value as number of doors")

        if door_numbers < 1:
            raise AttributeError("There should be 1 single door in the house construction")

        self.house_builder.doors = door_numbers
        return self

    def set_windows(self, window_numbers):
        if type(window_numbers) != int:
            raise AttributeError("Pass numerical value as number of windows")

        if window_numbers < 1:
            raise AttributeError("There should be 1 single window in the house construction")
        self.house_builder.windows = window_numbers
        return self

    def get_house(self):
        return self.house_builder
