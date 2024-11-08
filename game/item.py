class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, player):
        if self.effect == "heal":
            player.hp = min(player.hp + 20, 100)
            print("You used a potion and recovered 20 HP.")
        elif self.effect == "boost":
            player.attack += 5
            print("Your attack power increased!")
