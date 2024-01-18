from abc import ABC, abstractmethod


class GUIComponent(ABC):
    """This is the common Abstract Class for GUI Components, Abstract Factory"""

    @abstractmethod
    def create_button_gui_component(self):
        pass

    @abstractmethod
    def create_checkbox_gui_component(self):
        pass
