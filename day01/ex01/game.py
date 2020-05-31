class GotCharacter:
    def __init__(self, name, is_alive=True):
        if type(is_alive) is not bool:
            is_alive = True
        self.name = name
        self.is_alive = is_alive


class Lannister(GotCharacter):
    def __init__(self, name, is_alive=True):
        super().__init__(name, is_alive)
        self.family_name = 'Lannister'
        self.house_words = 'A Lannister always pays her/his debts.'

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
