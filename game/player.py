class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_hp = (self.level*10) + 80
        self.hp = (self.level*10) + 80
        self.attack = (self.level*5) + 20
        self.defense = self.level * 2
        self.position = (0, 0)  
        self.weapon = ("Knife", 1)
        self.healpotion = 0
        self.attackpotion = 0
        self.defensepotion = 0

    def level_up(self):
        self.level += 1

        percentage_hp = self.hp / self.max_hp

        self.max_hp = (self.level*10) + 80
        self.hp = int(self.max_hp * percentage_hp)

        self.attack = (self.level*5) + 20
        self.defense = (self.level * 2) + 5 
        print(f"You leveled up to level {self.level}!")
