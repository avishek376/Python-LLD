from Builder import *
from Product import *


class Director:

    @staticmethod
    def construct():
        return Builder().get_builder_a().get_builder_b().get_builder_c().get_product()
