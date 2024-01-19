"""
Client asking for specific chair
"""
from chair_factory import ChairFactory

chair = ChairFactory.get_chair("SmallChair")
print(chair.get_chair_dimention())
