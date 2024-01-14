from ICloneable import ICloneable
import copy


class User(ICloneable):
    """This is product or prototype class"""

    def __init__(self, id, name, email, phone_number):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def clone(self):
        return copy.copy(self)
