class House:
    """This class implements House as Product"""

    def __init__(self, building_type="Apartment", doors=2, windows=7, house_material="wall"):
        self.building_type = building_type
        self.doors = doors
        self.windows = windows
        self.house_material = house_material

    def construction(self):
        return f"This is a {self.building_type} house with {self.doors} doors and {self.windows} windows made of {self.house_material}"
