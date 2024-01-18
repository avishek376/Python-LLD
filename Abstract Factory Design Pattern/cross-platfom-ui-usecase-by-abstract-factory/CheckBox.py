from abc import ABC, abstractmethod


class CheckBox(ABC):
    """This is the common Abstract Class for Checkbox's"""

    @abstractmethod
    def create_checkbox(self):
        """This is the checkbox method"""
        pass
