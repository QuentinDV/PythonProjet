from game.player import Player
from game.map import GameMap
from game.menu import display_health,loose_menu,tutorial
from os import system

class GameManager:
    def __init__(self):
        self.running = True
        self.player = None
        self.game_map = GameMap()

    def start_new_game(self):
        name = input("Enter your name: ")
        self.player = Player(name=name)
        print(f"Welcome, {self.player.name}!")
        self.game_loop() 

    def load_saved_game(self):
        print("Loading saved game... (Not yet implemented)")

    def exit_game(self):
        print("Exiting the game...")
        self.running = False

    def game_menu(self):
        print(f"{self.player.name} | Lvl:{self.player.level}")
        print(display_health(self.player))

        print(f"Damage : {self.player.attack}")
        print(f"Weapon : {self.player.weapon[0]} | Damage x{self.player.weapon[1]}")

        self.game_map.display_surroundings(self.player)
        print("")

    def game_loop(self): 
        while self.player.hp > 0 and self.running:
            self.game_menu()
            command = input("Where do You Go ?: ").lower()
            system('cls')
            if command in ["north", "n", "z", "t"]:
                self.game_map.move_player(self.player, "north")
            elif command in ["south", "s"]:
                self.game_map.move_player(self.player, "south")
            elif command in ["east", "e", "r", "d"]:
                self.game_map.move_player(self.player, "east")
            elif command in ["west", "w", "l", "q"]:
                self.game_map.move_player(self.player, "west")
            elif command == "i":
                tutorial()
                input("Type 'Enter' to continue")
            elif command == "k":
                system('cls')
                tutorial()
                input("Type 'Enter' to continue :")
            elif command == "save":
                print("not implemented yet")
            elif command == "exit":
                self.running = False
            else:
                print("Invalid command!")
        if self.player.hp < 1 and self.running:
            loose_menu()