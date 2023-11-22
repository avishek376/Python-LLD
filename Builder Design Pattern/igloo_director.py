from house_builder import HouseBuilder


class IglooDirector:
    """
    Concrete class representation of IGLOO Director
    """

    @staticmethod
    def construct():
        return HouseBuilder()\
            .building_type("Ice")\
            .wall_material("Ice")\
            .no_of_doors(1)\
            .no_of_windows(0)\
            .get_house()
