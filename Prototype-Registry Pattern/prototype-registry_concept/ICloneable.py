from abc import ABC, abstractmethod


class ICloneable(ABC):

    @abstractmethod
    def clone(self):
        pass
