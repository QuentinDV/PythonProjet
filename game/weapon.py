class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    # Conversion de l'objet en dictionnaire
    def to_dict(self):
        return {
            "name": self.name,
            "damage": self.damage,
        }
    
    # Création de l'objet à partir d'un dictionnaire
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["damage"])