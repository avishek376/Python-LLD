from Button import IButton


class WindowsButtonImpl(IButton):
    """This class implements IButton interface"""

    def click(self, category):
        return f"Ohh yes!!!{category} button clicked by USER"
