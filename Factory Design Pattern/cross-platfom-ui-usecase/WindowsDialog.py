from Dialog import IDialog
from WindowsButton import WindowsButtonImpl


class WindowsDialogImpl(IDialog):

    def __init__(self):
        pass

    def factory(self):
        return WindowsButtonImpl()
