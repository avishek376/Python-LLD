from NavigationStrategy import NavigationStrategy


class Navigator:
    """This class represents navigator"""

    def __init__(self, navigator: NavigationStrategy) -> None:
        self._navigator = navigator

    def navigate(self, source, destination) -> None:
        self._navigator.navigate(source, destination)
