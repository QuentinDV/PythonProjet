class Inventory:
    def __init__(self):
        self.healpotion = 2
        self.attackpotion = 1
        self.defensepotion = 1
    
    def to_dict(self):
        return {
            "healpotion": self.healpotion,
            "attackpotion": self.attackpotion,
            "defensepotion": self.defensepotion,
        }
    
    @classmethod
    def from_dict(cls, data):
        inventory = cls()
        inventory.healpotion = data["healpotion"]
        inventory.attackpotion = data["attackpotion"]
        inventory.defensepotion = data["defensepotion"]
        return inventory

    