from interface_furniture_factory import IFurnitureFactory
from chair_factory import ChairFactory
from table_factory import TableFactory


class FurnitureFactory(IFurnitureFactory):
    """
    Factory Concrete Class
    to return a furniture
    """

    @staticmethod
    def get_furniture(furniture):
        try:
            if furniture in ["SmallChair", "MediumChair", "BigChair"]:
                return ChairFactory.get_chair(furniture)
            if furniture in ["RoundGlassTable", "SquareWoodenTable", "OvalStoneTable"]:
                return TableFactory.get_table(furniture)
            raise Exception("Wrong Selection of Furnitures")

        except Exception as _e:
            print(_e)
        return None

