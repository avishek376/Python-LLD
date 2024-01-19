from HouseBuilder import HouseBuilder


class CastleDirector:

    @staticmethod
    def construct():
        return HouseBuilder() \
            .set_building_type("Castle") \
            .set_house_material("Stone") \
            .set_doors(7) \
            .set_windows(11) \
            .get_house()
