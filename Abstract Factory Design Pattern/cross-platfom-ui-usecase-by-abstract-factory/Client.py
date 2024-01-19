from WindowsGUIComponent import WindowsGUIComponent
from IOSGUIComponent import IOSGUIComponent


class Client:
    """This is the client class"""
    windows_button_impl = WindowsGUIComponent().create_button_gui_component()
    print(windows_button_impl.create_button())
    windows_checkbox_impl = WindowsGUIComponent().create_checkbox_gui_component()
    print(windows_checkbox_impl.create_checkbox())
    print("*" * 27)
    ios_button_impl = IOSGUIComponent().create_button_gui_component()
    print(ios_button_impl.create_button())
    ios_checkbox_impl = IOSGUIComponent().create_checkbox_gui_component()
    print(ios_checkbox_impl.create_checkbox())
