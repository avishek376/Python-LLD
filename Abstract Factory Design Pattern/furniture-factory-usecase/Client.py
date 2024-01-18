from AbstractFurnitureFactory import FurnitureFactory as AbsFactory


class Client:
    table = AbsFactory().get_furniture("true-chair")
    print(table.create())
