from houseboat_director import HouseBoatDirector
from igloo_director import IglooDirector
"""
Client 
to get "PRODUCT" from Director class
"""

HOUSEBOAT = HouseBoatDirector.construct()
IGLOO = IglooDirector.construct()
print(HOUSEBOAT.construction())
print(IGLOO.construction())

