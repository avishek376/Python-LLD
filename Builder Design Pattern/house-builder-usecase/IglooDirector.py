from HouseBuilder import *


class IglooDirector:
    """One of the Director to implement complex representation"""

    @staticmethod
    def construct():
        return HouseBuilder(). \
            set_building_type("Igloo"). \
            set_house_material("Snow"). \
            set_doors(1). \
            set_windows(2). \
            get_house()
