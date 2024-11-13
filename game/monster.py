import random

class Monster:
    def __init__(self, level, isBoss = False):
        self.isBoss = isBoss
        self.level = level
        self.hp = level * 10 + 15
        self.max_hp = level * 10 + 15
        self.attack = level * 4
        self.defense = level * 1
        self.xp_given = level * 25  
        if not isBoss:
            self.name = random.choice(["Goblin", "Wolf", "Skeleton", "Orc", "Zombie", "Slime"])
        else:
            self.name = random.choice(["Dragon", "Demon", "Behemoth", "Hydra", "Giant", "Kraken"])
            self.hp *= 2
            self.max_hp *= 2
            self.attack *= 2
            self.defense *= 2
        
        

    def is_alive(self):
        return self.hp > 0
