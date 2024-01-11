from IBuilder import *
from Product import *


class Builder(IBuilder):
    def __init__(self):
        self.product = Product()

    def get_builder_a(self):
        self.product.parts.append('a')
        return self

    def get_builder_b(self):
        self.product.parts.append('b')
        return self

    def get_builder_c(self):
        self.product.parts.append('c')
        return self

    def get_product(self):
        return self.product
