from abc import ABC, abstractmethod


class Button(ABC):
    """This is the common Abstract Class for Buttons"""

    @abstractmethod
    def create_button(self):
        """This is the button method"""
        pass
