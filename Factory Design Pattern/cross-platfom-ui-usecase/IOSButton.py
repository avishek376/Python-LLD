from Button import IButton


class IOSButtonImpl(IButton):
    """This class implements bButton interface"""

    def click(self, category):
        return f"{category} button clicked by User"
