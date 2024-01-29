from NavigationStrategy import NavigationStrategy


class ByCarNavigation(NavigationStrategy):
    """This class implements the By Car Navigation Strategy"""

    def __init__(self) -> None:
        pass

    def navigate(self, source, destination) -> None:
        print(f"ByCarNavigation: Navigating from {source} to {destination} by car")
