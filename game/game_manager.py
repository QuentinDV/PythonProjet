from game.player import Player
from game.map import GameMap

class GameManager:
    def __init__(self):
        self.running = True
        self.player = None
        self.game_map = GameMap()

    def start_new_game(self):
        name = input("Enter your name: ")
        self.player = Player(name=name)
        print(f"Welcome, {self.player.name}!")
        self.game_loop()  # Appel de la méthode game_loop

    def load_saved_game(self):
        print("Loading saved game... (Not yet implemented)")

    def exit_game(self):
        print("Exiting the game...")
        self.running = False

    def game_loop(self):  # Ajout de la méthode game_loop
        while self.player.hp > 0 and self.running:
            self.game_map.describe_map(self.player.position)
            command = input("Command (North, South, East, West): ").lower()
            
            if command in ["north", "n"]:
                self.game_map.move_player(self.player, "north")
            elif command in ["south", "s"]:
                self.game_map.move_player(self.player, "south")
            elif command in ["east", "e"]:
                self.game_map.move_player(self.player, "east")
            elif command in ["west", "w"]:
                self.game_map.move_player(self.player, "west")
            else:
                print("Invalid command!")
