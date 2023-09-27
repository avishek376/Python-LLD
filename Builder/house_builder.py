from interface_house_builder import IHouseBuilder
from house_product import House


class HouseBuilder(IHouseBuilder):
    """
    The concrete representation of House Builder class
    """

    def __init__(self):
        self.house = House()

    def building_type(self, building_type):
        self.house.building_type = building_type
        return self

    def wall_material(self, wall_material):
        self.house.wall_material = wall_material
        return self

    def no_of_doors(self, no_of_doors):
        self.house.no_of_doors = no_of_doors
        return self

    def no_of_windows(self, no_of_windows):
        self.house.no_of_windows = no_of_windows
        return self

    def get_house(self):
        return self.house
