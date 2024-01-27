from CharFlyweight import CharFlyweight


class CharFactory:
    char_flyweights = {}

    @staticmethod
    def get_char(char):
        if char not in CharFactory.char_flyweights:
            CharFactory.char_flyweights[char] = CharFlyweight(char)
        return CharFactory.char_flyweights[char]
