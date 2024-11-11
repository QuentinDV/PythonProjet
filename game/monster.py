import random

class Monster:
    def __init__(self, level):
        self.level = level
        self.hp = level * 10 + 30
        self.max_hp = level * 10 + 30
        self.attack = level * 7
        self.defense = level * 2
        self.name = random.choice(["Goblin", "Wolf", "Skeleton"])

    def is_alive(self):
        return self.hp > 0
