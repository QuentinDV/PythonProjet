from os import system


# Codes de couleur ANSI
RESET = "\033[0m"
ORANGE = "\033[38;5;214m"
RED = "\033[91m" # POUR LE BOSS
GREEN = "\033[92m"
BROWN = "\033[38;5;94m"
DARK_GREEN = "\033[38;5;22m"
LIGHT_BLUE = "\033[96m"
GRAY_BLUE = "\033[38;5;67m"
GREY = "\033[38;5;245m"
ROSE = "\033[38;5;213m"

class Combat:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self.use_atk_potion = False
        self.use_dfc_potion = False

    def start(self):
        system('cls')
        print(f"{GREY}A wild {RED}{self.monster.name}{GREY} appears!")
        while self.player.hp > 0 and self.monster.hp > 0:
            print(f"{ORANGE}{self.player.name}{RESET} | {ROSE}Lvl:{RESET} {self.player.level}") 
            print(self.display_health(self.player.hp, self.player.max_hp))     
            print(f"{BROWN}Damage:{RESET} {self.player.attack} | {LIGHT_BLUE}Defense:{RESET} {self.player.defense}")
            print(f"{GRAY_BLUE}Weapon:{RESET} {self.player.weapon[0]}, {BROWN}Dmg:{RESET} x{self.player.weapon[1]}")
            print("")
            print(f"{RED}{self.monster.name}{RESET} | {ROSE}Lvl:{RESET} {self.monster.level}")
            print(self.display_health(self.monster.hp, self.monster.max_hp))

            action = input(f"{GREY}Attack 'a', Inventory 'i', Run 'r'{RESET}{DARK_GREEN} >{RESET}").lower()
            print(action)
            if action == "attack" or action == "a":
                self.player_attack()
            
            elif action == "i":
                self.inventory_menu()

            elif action == "hp":
                self.use_healpotion()

            elif action == "ap":
                self.use_attackpotion()

            elif action == "dp":
                self.use_defensepotion()

            elif action == "run" or action == "r":
                system('cls')
                print(f"{GREY}You fled the battle!{RESET}")
                return
            else:
                print(f"{GREY}Invalid action. Retry{RESET}")

        if self.player.hp <= 0:
            print("You have been defeated.")
        elif self.monster.hp <= 0:
            if self.use_atk_potion:
                self.player.attack -= 20
            if self.use_dfc_potion:
                self.player.defense -=10

            print(f"{ORANGE}You{GREY} defeated the {RED}monster!{RESET}")
            self.player.level_up()

    def inventory_menu(self):
        while True:
            system('cls')
            print(f"{ORANGE}{self.player.name}{RESET} | {ROSE}Lvl:{RESET} {self.player.level}")
            print(self.display_health(self.player.hp, self.player.max_hp))

            print(f"{BROWN}Damage:{RESET} {self.player.attack} | {LIGHT_BLUE}Defense:{RESET} {self.player.defense}")
            print(f"{GRAY_BLUE}Weapon:{RESET} {self.player.weapon[0]}, {BROWN}Dmg:{RESET} x{self.player.weapon[1]}")

            print(f"{GREY}Inventory :")
            if self.player.healpotion > 0: 
                print(f"{DARK_GREEN}Heal Potion:{RESET} x{self.player.healpotion} | {GREY}Type 'hp' to use one{RESET}")
            else:
                print(f"{DARK_GREEN}Heal Potion:{RESET} None")

            if self.player.attackpotion > 0: 
                print(f"{BROWN}Attack Potion:{RESET} x{self.player.attackpotion} | {GREY}Type 'ap' to use one{RESET}")
            else:
                print(f"{BROWN}Attack Potion:{RESET} None")

            if self.player.defensepotion > 0: 
                print(f"{LIGHT_BLUE}Defense Potion:{RESET} x{self.player.defensepotion} | {GREY}Type 'dp' to use one{RESET}")
            else:
                print(f"{LIGHT_BLUE}Defense Potion:{RESET} None")

            choice = input(f"{GREY}Type 'q' to quit the inventory{RESET} {DARK_GREEN}> {RESET}").lower()

            if choice == 'hp':
                system('cls')
                self.use_healpotion()
                break
            elif choice == 'ap':
                system('cls')
                self.use_attackpotion()
                break
            elif choice == 'dp':
                system('cls')
                self.use_defensepotion()
                break
            elif choice == 'q':
                system('cls')
                print(f"{GREY}You closed the inventory.{RESET}")
                break
            else:
                system('cls')
                print(f"{GREY}Invalid input. Try again.{RESET}")



    def use_healpotion(self):
        if self.player.healpotion > 0:
            self.player.healpotion -= 1
            self.player.hp = min(self.player.hp + 20, self.player.max_hp)
            print(f"{ORANGE}You {GREY}used a {DARK_GREEN}heal potion{GREY} and recovered {GREEN}20 HP.{RESET}")

            if self.monster.hp > 0:
                monsterdamage = int(max(self.monster.attack - self.player.defense, 0))
                self.player.hp -= monsterdamage
                system('cls')
                print(f"{GREY}The {RED}{self.monster.name}{GREY} dealt {BROWN}{monsterdamage} damage{GREY} to {ORANGE}You.{RESET}")
        else:
            print(f"{ORANGE}You{GREY} have no {DARK_GREEN}heal potions{GREY} left!{RESET}")     

    def use_attackpotion(self):
        if self.player.attackpotion > 0:
            self.player.attackpotion -= 1
            self.player.attack += 20
            self.use_atk_potion = True
            print(f"{ORANGE}You {GREY}used an {BROWN}Attack Potion{GREY} and gained {BROWN}20 attack power{GREY} until the end of the combat!{RESET}")

            if self.monster.hp > 0:
                monsterdamage = int(max(self.monster.attack - self.player.defense, 0))
                self.player.hp -= monsterdamage
                system('cls')
                print(f"{GREY}The {RED}{self.monster.name}{GREY} dealt {BROWN}{monsterdamage} damage{GREY} to {ORANGE}You.{RESET}")
        else:
            print(f"{ORANGE}You{GREY} have no {BROWN}Attack Potions{GREY} left!{RESET}")

    def use_defensepotion(self):
        if self.player.defensepotion > 0:
            self.player.defensepotion -= 1
            self.player.defense += 10
            self.use_dfc_potion = True
            print(f"{ORANGE}You {GREY}used a {LIGHT_BLUE}Defense Potion{GREY} and gained {LIGHT_BLUE}10 defense{GREY} until the end of the combat!{RESET}")

            if self.monster.hp > 0:
                monsterdamage = int(max(self.monster.attack - self.player.defense, 0))
                self.player.hp -= monsterdamage
                system('cls')
                print(f"{GREY}The {RED}{self.monster.name}{GREY} dealt {BROWN}{monsterdamage} damage{GREY} to {ORANGE}You.{RESET}")
        else:
            print(f"{ORANGE}You{GREY} have no {LIGHT_BLUE}Defense Potions{GREY} left!{RESET}")

    def display_health(self,current_hp,max_hp):
        full_blocks = int(current_hp // 10)
        empty_blocks = int((max_hp // 10) - full_blocks)

        health_bar = "▮" * full_blocks + "▯" * empty_blocks

        return f"{GREEN}HP:{RESET} [{health_bar} ] {current_hp}/{max_hp}"

    def player_attack(self):
        playerdamage = int(max(self.player.attack * self.player.weapon[1] - self.monster.defense, 0))
        self.monster.hp -= playerdamage
        if self.monster.hp > 0:
            monsterdamage = int(max(self.monster.attack - self.player.defense, 0))
            self.player.hp -= monsterdamage
            system('cls')
            print(f"{ORANGE}You{RESET} dealt {BROWN}{playerdamage} damage{RESET} to the {RED}{self.monster.name}{RESET} " +
                  f"/ The {RED}{self.monster.name}{RESET} dealt {BROWN}{monsterdamage} damage{RESET} to {ORANGE}You.{RESET}")
        
