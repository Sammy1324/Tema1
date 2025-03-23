from Character import Character

class Human(Character):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
        self.armor = 2