class Combat:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def start(self):
        print(f"A wild {self.monster.name} appears!")
        while self.player.hp > 0 and self.monster.hp > 0:
            action = input("Choose action: (Attack, Run): ").lower()
            if action == "attack":
                self.player_attack()
            elif action == "run":
                print("You fled the battle!")
                return
            else:
                print("Invalid action.")

            if self.monster.hp > 0:
                self.monster_attack()

        if self.player.hp <= 0:
            print("You have been defeated.")
        elif self.monster.hp <= 0:
            print("You defeated the monster!")
            self.player.gain_xp(10)

    def player_attack(self):
        damage = max(self.player.attack - self.monster.defense, 0)
        self.monster.hp -= damage
        print(f"You dealt {damage} damage to the {self.monster.name}.")

    def monster_attack(self):
        damage = max(self.monster.attack - self.player.defense, 0)
        self.player.hp -= damage
        print(f"The {self.monster.name} dealt {damage} damage to you.")
