from Charachter import Character
from CharFactory import CharFactory

if __name__ == '__main__':
    # Client code
    characters = []
    characters.append(Character('A', 12))
    characters.append(Character('B', 14))
    characters.append(Character('A', 12))  # Reusing 'A' from flyweight

    for character in characters:
        character.render()

    for k, v in CharFactory.char_flyweights.items():
        print(k, v)