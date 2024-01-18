from GUIComponent import GUIComponent
from WindowsButton import WindowsButtonImpl
from WindowsCheckBox import WindowsCheckBoxImpl


class WindowsGUIComponent(GUIComponent):
    """This is the Windows GUI Component Class"""

    def __init__(self):
        pass

    def create_button_gui_component(self):
        """This is the implementation of Windows create_button_gui_component method"""
        return WindowsButtonImpl()

    def create_checkbox_gui_component(self):
        """This is the implementation of Windows create_checkbox_gui_component method"""
        return WindowsCheckBoxImpl()
