

# Codes de couleur ANSI
RESET = "\033[0m"
ORANGE = "\033[38;5;214m"
ROSE = "\033[38;5;213m"
GREY = "\033[38;5;245m"

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_hp = (self.level*10) + 80
        self.hp = (self.level*10) + 80
        self.attack = (self.level*5) + 20
        self.defense = self.level * 2
        self.position = (0, 0)  
        self.weapon = ("Knife", 0.75)
        self.healpotion = 1
        self.attackpotion = 0
        self.defensepotion = 0
        self.xp = 0  
        self.xp_to_level_up = 10  

    def add_xp(self, amount):
        self.xp += amount
        if self.xp >= self.xp_to_level_up:  
            self.level += 1
            self.xp -= self.xp_to_level_up  
            self.xp_to_level_up = int(self.xp_to_level_up * 1.5)  

            percentage_hp = self.hp / self.max_hp
            self.max_hp = (self.level*10) + 80
            self.hp = int(self.max_hp * percentage_hp)

            self.attack = (self.level*5) + 20
            self.defense = (self.level * 2) + 5
            return True
        
        else:
            return False
            
