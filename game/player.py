class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.defense = 5
        self.level = 1
        self.xp = 0
        self.position = (0, 0)  # Position de départ
        self.inventory = ["Knife"]

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 10:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hp += 20
        self.attack += 5
        self.defense += 3
        print(f"{self.name} has leveled up to level {self.level}!")
