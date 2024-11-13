class Inventory:
    def __init__(self):
        self.healpotion = 1
        self.attackpotion = 0
        self.defensepotion = 0
    
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

    