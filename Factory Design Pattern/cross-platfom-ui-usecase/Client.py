from WindowsDialog import WindowsDialogImpl
from IOSDialog import IOSDialogImpl


class Client:
    """This is client class only knows about factories, doesn't know about the implementation of Button class"""

    windows_factory = WindowsDialogImpl().factory()
    print(windows_factory.click("Windows"))

    ios_factory = IOSDialogImpl().factory()
    print(ios_factory.click("IOS"))
