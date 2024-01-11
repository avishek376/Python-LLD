from Builder import *
from Product import *


class Director:
    """This class creates the Product based on client requirement"""

    @staticmethod
    def construct():
        return Builder().get_builder_a().get_builder_b().get_builder_c().get_product()
