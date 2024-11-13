from game.inventory import Inventory
from game.weapon import Weapon

# Codes de couleur ANSI
RESET = "\033[0m"
ORANGE = "\033[38;5;214m"
ROSE = "\033[38;5;213m"
GREY = "\033[38;5;245m"

class Player:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0)  
        self.level = 1
        self.max_hp = (self.level*10) + 80
        self.hp = (self.level*10) + 80
        self.attack = (self.level*5) + 20
        self.defense = self.level * 2
        self.weapon = Weapon("Knife", 0.75)
        self.inventory = Inventory()
        self.xp = 0  
        self.xp_to_level_up = 10  
        self.win = False

    def to_dict(self):
        return {
            "name": self.name,
            "position": self.position,
            "level": self.level,
            "max_hp": self.max_hp,
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "weapon": self.weapon.to_dict() if self.weapon else None,
            "inventory": self.inventory.to_dict(),
            "xp": self.xp,
            "xp_to_level_up": self.xp_to_level_up,
        }
    
    @classmethod
    def from_dict(cls, data):
        player = cls(data["name"])
        player.position = tuple(data["position"])
        player.level = data["level"]
        player.max_hp = data["max_hp"]
        player.hp = data["hp"]
        player.attack = data["attack"]
        player.defense = data["defense"]
        player.weapon = Weapon(data["weapon"]["name"], data["weapon"]["damage"])
        player.inventory = Inventory()
        player.inventory.healpotion = data["inventory"]["healpotion"]
        player.inventory.attackpotion = data["inventory"]["attackpotion"]
        player.inventory.defensepotion = data["inventory"]["defensepotion"]
        player.xp = data["xp"]
        player.xp_to_level_up = data["xp_to_level_up"]
        return player

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
            
