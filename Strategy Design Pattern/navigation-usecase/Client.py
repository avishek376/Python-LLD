from ByCarNavigationStrategy import ByCarNavigation
from ByBikeNavigationStrategy import ByBikeNavigation
from ByWalkNavigationStrategy import ByWalkNavigation
from Navigator import Navigator

if __name__ == '__main__':
    navigator = Navigator(ByCarNavigation())
    navigator.navigate("Delhi", "Mumbai")
