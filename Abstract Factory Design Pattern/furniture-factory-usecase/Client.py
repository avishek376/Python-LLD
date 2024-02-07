from AbstractFurnitureFactory import FurnitureFactory as AbsFactory


class Client:
    try:
        table = AbsFactory().get_furniture("modern-table")
        if table:
            print(table.create())
    except ValueError as e:
        print(e)
