from abc import ABC, abstractmethod


class IRegister(ABC):
    """This is a Register Interface """

    @abstractmethod
    def get_prototype(self, role):
        """To get the prototype instance"""
        pass

    @abstractmethod
    def add_prototype(self, role, user):
        """To add prototype in register"""
        pass

    def clone(self, role):
        prototype = self.get_prototype(role)
        if prototype is None:
            raise Exception(f"The role {role} is not present")
        return prototype.clone()
