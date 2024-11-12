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
        print(f"{ORANGE}{self.player.name}{RESET} | {ROSE}Lvl:{RESET} {self.player.level} | {ROSE}{self.player.xp}/{self.player.xp_to_level_up} {GREY}XP{RESET}")
        print(display_health(self.player))

        print(f"{BROWN}Damage:{RESET} {self.player.attack} | {LIGHT_BLUE}Defense:{RESET} {self.player.defense}")
        print(f"{GRAY_BLUE}Weapon:{RESET} {self.player.weapon[0]}, {BROWN}Dmg:{RESET} x{self.player.weapon[1]}")

        self.game_map.display_surroundings(self.player)
    
    def inventory_menu(self):
        system('cls')
        print(f"{ORANGE}{self.player.name}{RESET} | {ROSE}Lvl:{RESET} {self.player.level} | {ROSE}{self.player.xp}/{self.player.xp_to_level_up} {GREY}XP{RESET}")
        print(display_health(self.player))

        print(f"{BROWN}Damage:{RESET} {self.player.attack} | {LIGHT_BLUE}Defense:{RESET} {self.player.defense}")
        print(f"{GRAY_BLUE}Weapon:{RESET} {self.player.weapon[0]}, {BROWN}Dmg:{RESET} x{self.player.weapon[1]}")

        print(f"{GREY}Inventory :")
        if self.player.healpotion > 0: 
            print(f"{DARK_GREEN}Heal Potion:{RESET} x{self.player.healpotion} | {GREY}Type 'hp' after 'Enter' to use one{RESET}")
        else:
            print("")
        if self.player.attackpotion > 0: 
            print(f"{BROWN}Attack Potion:{RESET} x{self.player.attackpotion}")
        else:
            print("")
        if self.player.defensepotion > 0: 
            print(f"{LIGHT_BLUE}Defense Potion:{RESET} x{self.player.defensepotion}")
        else:
            print("")


    def game_loop(self): 
        system('cls')
        print(f"{GREY}Welcome, {ORANGE}{self.player.name}{RESET}!")

        while self.player.hp > 0 and self.running:
            self.game_menu()
            command = input(f"{GREY}Type 'H' For Help{GREY} {DARK_GREEN}>{RESET}").lower()
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
                input(f"{GREY}Type 'Enter' to continue {DARK_GREEN}>{RESET}")
                system('cls')
                print('')

            elif command == "hp":
                self.use_healpotion()

            elif command == "h":
                system('cls')
                tutorial()
                input(f"{GREY}Type 'Enter' to continue {DARK_GREEN}>{RESET}")
                system('cls')
                print('')

            elif command == "save":
                print("not implemented yet")

            elif command == "exit":
                self.running = False

            else:
                print(f"{GREY}Invalid command!{RESET}")

        if self.player.hp < 1 and self.running:
            loose_menu()

    def use_healpotion(self):
        if self.player.healpotion > 0:
            self.player.healpotion -= 1
            self.player.hp = min(self.player.hp + 20, self.player.max_hp)
            print("You used a potion and recovered 20 HP.")
        else:
            print("You have no potions left!")