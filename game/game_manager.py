from game.player import Player
from game.map import GameMap
from game.menu import display_health,loose_menu,tutorial,win_menu
from data.save import Save,Load
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

    # Conversion de l'objet en dictionnaire
    def to_dict(self):
        return {
            "player": self.player.to_dict() if self.player else None,
            "game_map": self.game_map.to_dict(),
        }

    # Création d'une nouvelle partie
    def start_new_game(self):
        name = input(f"{ORANGE}Enter your name: {RESET}").upper()
        self.player = Player(name=name)
        self.game_loop() 

    # Chargement d'une partie sauvegardée
    def load_saved_game(self):
        print(f"{GREY}Choose Save Number :")
        save1 = Load("1").is_save()
        save2 = Load("2").is_save()
        save3 = Load("3").is_save()

        if save1:
            print(f"{DARK_GREEN}1. {ORANGE}{save1[0]}{GREY} | {ROSE}Lvl:{RESET}{save1[1]}{GREY} | {GRAY_BLUE}{save1[2]}{RESET}")
        else:
            print(f"{DARK_GREEN}1. {GREY}Empty{RESET}")

        if save2:   
            print(f"{DARK_GREEN}2. {ORANGE}{save2[0]}{GREY} | {ROSE}Lvl:{RESET}{save2[1]}{GREY} | {GRAY_BLUE}{save2[2]}{RESET}")
        else:
            print(f"{DARK_GREEN}2. {GREY}Empty{RESET}")

        if save3:
            print(f"{DARK_GREEN}3. {ORANGE}{save3[0]}{GREY} | {ROSE}Lvl:{RESET}{save3[1]}{GREY} | {GRAY_BLUE}{save3[2]}{RESET}")
        else:
            print(f"{DARK_GREEN}3. {GREY}Empty{RESET}")

        save_number = input(f"{GREY}Enter the save number ({DARK_GREEN}'1'{GREY}, {DARK_GREEN}'2'{GREY}, {DARK_GREEN}'3'{GREY}) {DARK_GREEN}> {RESET}")

        if save_number not in ["1", "2", "3"]:
            print(f"{GREY}Invalid save number!{RESET}")
            return
        
        if not Load(save_number).is_save():
            print(f"{GREY}This save is empty!{RESET}")
            return

        save = Load(save_number)
        save.json_load()

        self.player = save.player
        self.game_map = save.game_map
        self.game_loop()

    # Quitter le jeu
    def exit_game(self):
        print("Exiting the game...")
        self.running = False

    # Menu en Jeu
    def game_menu(self):
        print(f"{ORANGE}{self.player.name}{RESET} | {ROSE}Lvl:{RESET} {self.player.level} | {ROSE}{self.player.xp}/{self.player.xp_to_level_up} {GREY}XP{RESET}")
        print(display_health(self.player))

        print(f"{BROWN}Damage:{RESET} {self.player.attack} | {LIGHT_BLUE}Defense:{RESET} {self.player.defense}")
        print(f"{GRAY_BLUE}Weapon:{RESET} {self.player.weapon.name}, {BROWN}Dmg:{RESET} x{self.player.weapon.damage}")

        self.game_map.display_surroundings(self.player)
    
    # Menu d'inventaire
    def inventory_menu(self):
        system('cls')
        print(f"{ORANGE}{self.player.name}{RESET} | {ROSE}Lvl:{RESET} {self.player.level} | {ROSE}{self.player.xp}/{self.player.xp_to_level_up} {GREY}XP{RESET}")
        print(display_health(self.player))

        print(f"{BROWN}Damage:{RESET} {self.player.attack} | {LIGHT_BLUE}Defense:{RESET} {self.player.defense}")
        print(f"{GRAY_BLUE}Weapon:{RESET} {self.player.weapon.name}, {BROWN}Dmg:{RESET} x{self.player.weapon.damage}")

        print(f"{GREY}Inventory :")
        if self.player.inventory.healpotion > 0: 
            print(f"{DARK_GREEN}Heal Potion:{RESET} x{self.player.inventory.healpotion} | {GREY}Type 'hp' after 'Enter' to use one{RESET}")
        else:
            print("")
        if self.player.inventory.attackpotion > 0: 
            print(f"{BROWN}Attack Potion:{RESET} x{self.player.inventory.attackpotion}")
        else:
            print("")
        if self.player.inventory.defensepotion > 0: 
            print(f"{LIGHT_BLUE}Defense Potion:{RESET} x{self.player.inventory.defensepotion}")
        else:
            print("")

    # Menu de sauvegarde
    def save_menu(self):
        system('cls')
        print(f"{ORANGE}{self.player.name}{RESET} | {ROSE}Lvl:{RESET} {self.player.level} | {ROSE}{self.player.xp}/{self.player.xp_to_level_up} {GREY}XP{RESET}")
        print(display_health(self.player))

        print(f"{BROWN}Damage:{RESET} {self.player.attack} | {LIGHT_BLUE}Defense:{RESET} {self.player.defense}")
        print(f"{GRAY_BLUE}Weapon:{RESET} {self.player.weapon.name}, {BROWN}Dmg:{RESET} x{self.player.weapon.damage}")

        print(f"{GREY}Choose Save Number :")
        save1 = Load("1").is_save()
        save2 = Load("2").is_save()
        save3 = Load("3").is_save()

        if save1:
            print(f"{DARK_GREEN}1. {ORANGE}{save1[0]}{GREY} | {ROSE}Lvl:{RESET}{save1[1]}{GREY} | {GRAY_BLUE}{save1[2]}{RESET}")
        else:
            print(f"{DARK_GREEN}1. {GREY}Empty{RESET}")

        if save2:   
            print(f"{DARK_GREEN}2. {ORANGE}{save2[0]}{GREY} | {ROSE}Lvl:{RESET}{save2[1]}{GREY} | {GRAY_BLUE}{save2[2]}{RESET}")
        else:
            print(f"{DARK_GREEN}2. {GREY}Empty{RESET}")

        if save3:
            print(f"{DARK_GREEN}3. {ORANGE}{save3[0]}{GREY} | {ROSE}Lvl:{RESET}{save3[1]}{GREY} | {GRAY_BLUE}{save3[2]}{RESET}")
        else:
            print(f"{DARK_GREEN}3. {GREY}Empty{RESET}")

        save_number = input(f"{GREY}Enter the save number ({DARK_GREEN}'1'{GREY}, {DARK_GREEN}'2'{GREY}, {DARK_GREEN}'3'{GREY}) {DARK_GREEN}> {RESET}")

        if save_number not in ["1", "2", "3"]:
            print(f"{GREY}Invalid save number!{RESET}")
            return
        
        return save_number

    # Jeu
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
                save_number = self.save_menu()
                if save_number is not None:
                    Save(self).json_save(save_number)
                    print(f"{GREY}Game saved as {save_number}{RESET}")
                    break
                else:
                    print(f"{GREY}Error! Game not saved.{RESET}")

            elif command == "exit":
                self.running = False

            else:
                print(f"{GREY}Invalid command!{RESET}")

            if self.player.win and self.running:
                win_menu()
                self.running = False

        if self.player.hp < 1 and self.running:
            loose_menu()

    # Utilisation d'une potion de soin
    def use_healpotion(self):
        if self.player.inventory.healpotion > 0:
            self.player.inventory.healpotion -= 1
            self.player.hp = min(self.player.hp + 20, self.player.max_hp)
            print("You used a potion and recovered 20 HP.")
        else:
            print("You have no potions left!")