from Dialog import IDialog
from IOSButton import IOSButtonImpl


class IOSDialogImpl(IDialog):

    def __init__(self):
        pass

    def factory(self):
        return IOSButtonImpl()
