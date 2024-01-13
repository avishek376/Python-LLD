from Builder import *
from Product import *


class Director:
    """This class creates the Product based on client requirement"""

    @staticmethod
    def construct():
        return Builder().build_part_a().build_part_b().build_part_c().get_product()
