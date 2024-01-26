from IglooDirector import IglooDirector
from CastleDirector import CastleDirector

if __name__ == "__main__":
    iglooDirector = IglooDirector.construct()
    print(iglooDirector.construction())

    castleDirector = CastleDirector.construct()
    print(castleDirector.construction())
