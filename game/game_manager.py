from game.player import Player
from game.map import GameMap
from game.menu import display_health,loose_menu,tutorial
from os import system

# Codes de couleur ANSI
RESET = "\033[0m"
ORANGE = "\033[38;5;214m"
GREEN = "\033[92m"
ROSE = "\033[38;5;213m"
BROWN = "\033[38;5;94m"
LIGHT_BLUE = "\033[96m"
GRAY_BLUE = "\033[38;5;67m"
DARK_GREEN = "\033[38;5;22m"
GREY = "\033[38;5;245m"

class GameManager:
    def __init__(self):
        self.running = True
        self.player = None
        self.game_map = GameMap()

    def start_new_game(self):
        name = input(f"{ORANGE}Enter your name: {RESET}").upper()
        self.player = Player(name=name)
        self.game_loop() 

    def load_saved_game(self):
        print("Loading saved game... (Not yet implemented)")

    def exit_game(self):
        print("Exiting the game...")
        self.running = False

    def game_menu(self):
        print(f"{ORANGE}{self.player.name}{RESET} | {ROSE}Lvl:{RESET} {self.player.level}")
        print(display_health(self.player))

        print(f"{BROWN}Damage:{RESET} {self.player.attack} | {LIGHT_BLUE}Defense:{RESET} {self.player.defense}")
        print(f"{GRAY_BLUE}Weapon:{RESET} {self.player.weapon[0]}, {BROWN}Dmg:{RESET} x{self.player.weapon[1]}")

        self.game_map.display_surroundings(self.player)
    
    def inventory_menu(self):
        system('cls')
        print(f"{self.player.name} | Lvl:{self.player.level}")
        print(display_health(self.player))

        print(f"Damage : {self.player.attack} | Defense : {self.player.defense}")
        print(f"Weapon : {self.player.weapon[0]} | Damage x{self.player.weapon[1]}")

        print("Inventory :")
        if self.player.healpotion > 0: 
            print(f"Heal Potion : x{self.player.healpotion} | Type 'hp' to use one ")
        else:
            print("")
        if self.player.attackpotion > 0: 
            print(f"Attack Potion : x{self.player.attackpotion}")
        else:
            print("")
        if self.player.defensepotion > 0: 
            print(f"Heal Potion : x{self.player.defensepotion}")
        else:
            print("")
        print(f"{GREY}Type 'H' For Help")


    def game_loop(self): 
        system('cls')
        print(f"{GREY}Welcome, {ORANGE}{self.player.name}{RESET}!")

        while self.player.hp > 0 and self.running:
            self.game_menu()
            print(f"{GREY}Type 'H' For Help")
            command = input(f"{GREEN}>{RESET}").lower()
            system('cls')

            if command in ["north", "n", "z", "t"]:
                self.game_map.move_player(self.player, "north")
            elif command in ["south", "s", "b"]:
                self.game_map.move_player(self.player, "south")
            elif command in ["east", "e", "r", "d"]:
                self.game_map.move_player(self.player, "east")
            elif command in ["west", "w", "l", "q"]:
                self.game_map.move_player(self.player, "west")

            elif command == "i":
                self.inventory_menu()
                input(f"{DARK_GREEN}Type 'Enter' to continue >")
                system('cls')
                print('')

            elif command == "hp":
                self.use_healpotion()

            elif command == "h":
                system('cls')
                tutorial()
                input(f"{DARK_GREEN}Type 'Enter' to continue >")
                system('cls')
                print('')

            elif command == "save":
                print("not implemented yet")

            elif command == "exit":
                self.running = False

            else:
                print("Invalid command!")

        if self.player.hp < 1 and self.running:
            loose_menu()

    def use_healpotion(self):
        if self.player.healpotion > 0:
            self.player.healpotion -= 1
            self.player.hp = min(self.player.hp + 20, self.player.max_hp)
            print("You used a potion and recovered 20 HP.")
        else:
            print("You have no potions left!")