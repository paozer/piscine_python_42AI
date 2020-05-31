class GotCharacter:
    def __init__(self, name, is_alive):
        self.name = name
        if is_alive is None or type(is_alive) is not bool:
            is_alive = True
        self.is_alive = is_alive


class Lannister(GotCharacter):
    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

    def __init__(self, name, is_alive):
        super().__init__(name, is_alive)
        self.family_name = 'Lannister'
        self.house_words = 'A Lannister always pays her/his debts.'
