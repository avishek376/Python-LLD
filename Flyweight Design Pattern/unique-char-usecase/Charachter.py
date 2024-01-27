from CharFactory import CharFactory


class Character:
    """This class represents the Character class, extrinsic state of character"""

    def __init__(self, char, font_size):
        self.char_flyweight = CharFactory.get_char(char)
        self.font_size = font_size

    def render(self):
        print(f"Character: {self.char_flyweight.char}, Font Size: {self.font_size}")
