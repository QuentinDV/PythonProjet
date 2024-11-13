import json
from game.player import Player
from game.map import GameMap

# Codes de couleur ANSI
RESET = "\033[0m"
GREY = "\033[38;5;245m"

class Save:
    def __init__(self,game_state):
        self.game = game_state

    def json_save(self, filenb):
        with open(f"data/save_{filenb}.json", 'w') as f:
            json.dump(self.game.to_dict(), f, indent=4)
            print(f"{GREY}Game saved as {filenb}{RESET}")

class Load:
    def __init__(self,save_nb):
        self.save_nb = save_nb
        self.player = None
        self.game_map = None
    
    def json_load(self):
        with open(f"data/save_{self.save_nb}.json", 'r') as f:
            data = json.load(f)
            self.player = Player.from_dict(data["player"])
            self.game_map = GameMap.from_dict(data["game_map"])
            print(f"{GREY}Game loaded from save {self.save_nb}{RESET}")

    def is_save(self):
        try:
            with open(f"data/save_{self.save_nb}.json", 'r') as f:
                content = f.read().strip()
                if not content:
                    return False
                data = json.loads(content)  
                return data["player"]["name"], data["player"]["level"], data["player"]["weapon"]["name"]
        except (FileNotFoundError, json.JSONDecodeError):
            return False
            

        