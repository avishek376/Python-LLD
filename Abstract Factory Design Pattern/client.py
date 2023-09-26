from furniture_factory import FurnitureFactory

"""
Based on requirement client will get the Tables and Chairs
"""
FURNITURE = FurnitureFactory.get_furniture("SmallChair")
print(FURNITURE.build_chair())

FURNITURE = FurnitureFactory.get_furniture("SquareWoodenTable")
print(FURNITURE.build_table())
