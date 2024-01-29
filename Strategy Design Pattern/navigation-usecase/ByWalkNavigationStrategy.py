from NavigationStrategy import NavigationStrategy


class ByWalkNavigation(NavigationStrategy):
    """This class implements the By Walk Navigation Strategy"""

    def __init__(self) -> None:
        pass

    def navigate(self, source, destination) -> None:
        print(f"ByWalkNavigation: Navigating from {source} to {destination} by walk")