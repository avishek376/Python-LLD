class House:
    """
    The Concrete House Product representation
    """

    def __init__(self, building_type="Apartment", wall_material="Brick", no_of_doors=1, no_of_windows=0):
        self.building_type = building_type
        self.wall_material = wall_material
        self.no_of_doors = no_of_doors
        self.no_of_windows = no_of_windows

    def construction(self):
        return f"This is a {self.wall_material}" \
               f"{self.building_type} with " \
               f"{self.no_of_doors} doors and "\
                f"{self.no_of_windows} windows"
