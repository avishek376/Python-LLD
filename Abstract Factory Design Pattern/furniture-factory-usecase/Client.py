from AbstractFurnitureFactory import FurnitureFactory as AbsFactory


class Client:
    try:
        table = AbsFactory().get_furniture("normal-chair")
        if table:
            print(table.create())
    except ValueError as e:
        print(e)
