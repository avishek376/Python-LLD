from IRegister import *


class UserRegisterImpl(IRegister):
    """This class is the Prototype Implementation class"""

    def __init__(self):
        self._prototype = {}

    def get_prototype(self, role):
        """This method provides prototype from the Registry"""
        if role not in self._prototype:
            return None
        return self._prototype[role]

    def add_prototype(self, role, user):
        """This method add a prototype to a registry"""
        self._prototype[role] = user



