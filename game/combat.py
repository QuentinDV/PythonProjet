from os import system

class Combat:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def start(self):
        system('cls')
        print(f"\033[91mA wild {self.monster.name} appears!\033[0m")
        while self.player.hp > 0 and self.monster.hp > 0:
            print(f"{self.player.name} | Lvl:{self.player.level}")
            print(self.display_health(self.player.hp, self.player.max_hp))
            print(f"Damage : {self.player.attack} | Defense : {self.player.defense}")
            print(f"Weapon : {self.player.weapon[0]} | Potion x{self.player.healpotion}")
            print("")
            print(f"{self.monster.name} | Lvl:{self.monster.level}")
            print(self.display_health(self.monster.hp, self.monster.max_hp))
            print(f"Damage : {self.monster.attack} | Defense : {self.monster.defense}") 

            action = input("Choose action: (Attack, Use Potion, Run): ").lower()
            print(action)
            if action == "attack" or action == "a":
                self.player_attack()
            elif action == "use potion" or action == "p":
                self.use_potion()
            elif action == "run" or action == "r":
                system('cls')
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
            self.player.level_up()

    def use_potion(self):
        if self.player.healpotion > 0:
            self.player.healpotion -= 1
            self.player.hp = min(self.player.hp + 20, self.player.max_hp)
            print("You used a potion and recovered 20 HP.")
        else:
            print("You have no potions left!")

    def display_health(self,current_hp,max_hp):
        full_blocks = current_hp // 10
        empty_blocks = (max_hp // 10) - full_blocks

        health_bar = "▮" * full_blocks + "▯" * empty_blocks

        return f"HP: [{health_bar} ] {current_hp}/{max_hp}"


    def player_attack(self):
        damage = max(self.player.attack*self.player.weapon[1] - self.monster.defense, 0)
        self.monster.hp -= damage
        system('cls')
        print(f"You dealt {damage} damage to the {self.monster.name}.")

    def monster_attack(self):
        damage = max(self.monster.attack - self.player.defense, 0)
        self.player.hp -= damage
        system('cls')
        print(f"The {self.monster.name} dealt {damage} damage to you.")