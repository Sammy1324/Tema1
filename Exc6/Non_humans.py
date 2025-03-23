from Character import Character

class Non_human(Character):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
        self.armor = 2
        self.shield = 2