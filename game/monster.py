import random

class Monster:
    def __init__(self, level):
        self.level = level
        self.hp = level * 10 + 15
        self.max_hp = level * 10 + 15
        self.attack = level * 4
        self.defense = level * 1
        self.xp_given = level * 25  
        self.name = random.choice(["Goblin", "Wolf", "Skeleton", "Orc", "Zombie", "Slime"])

    def is_alive(self):
        return self.hp > 0
