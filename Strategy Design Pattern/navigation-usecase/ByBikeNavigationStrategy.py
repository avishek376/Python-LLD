from NavigationStrategy import NavigationStrategy


class ByBikeNavigation(NavigationStrategy):
    """This class implements the By Bike Navigation Strategy"""

    def __init__(self) -> None:
        pass

    def navigate(self, source, destination) -> None:
        print(f"ByBikeNavigation: Navigating from {source} to {destination} by bike")
