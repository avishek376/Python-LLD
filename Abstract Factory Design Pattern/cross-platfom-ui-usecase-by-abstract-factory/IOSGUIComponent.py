from GUIComponent import GUIComponent
from IOSButton import IOSButtonImpl
from IOSCheckBox import IOSCheckBoxImpl


class IOSGUIComponent(GUIComponent):
    """This class is the implementation of IOS GUI Component"""

    def __init__(self):
        pass

    def create_button_gui_component(self):
        """This is the implementation of Windows create_button_gui_component method"""
        return IOSButtonImpl()

    def create_checkbox_gui_component(self):
        """This is the implementation of Windows create_checkbox_gui_component method"""
        return IOSCheckBoxImpl()
