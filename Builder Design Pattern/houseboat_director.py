from house_builder import HouseBuilder


class HouseBoatDirector:
    """
    Concrete class of Director Class
    """

    @staticmethod
    def construct():
        """
        Construct and return the final product
        """
        return HouseBuilder() \
            .building_type("House Boat") \
            .wall_material("Wood") \
            .no_of_doors(2) \
            .no_of_windows(4) \
            .get_house()
