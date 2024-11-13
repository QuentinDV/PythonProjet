from game.monster import Monster  
from game.combat import Combat
from game.weapon import Weapon
from os import system


# Codes de couleur ANSI
RESET = "\033[0m"
ORANGE = "\033[38;5;214m"
RED = "\033[91m" # POUR LE BOSS
BROWN = "\033[38;5;94m"
DARK_GREEN = "\033[38;5;22m"
LIGHT_BLUE = "\033[96m"
GRAY_BLUE = "\033[38;5;67m"
GREY = "\033[38;5;245m"


class GameMap:
    def __init__(self):
        self.map_data = [
            ["@", ".", "!", ".", "#", "!", ".", ".", ".", "!", "h", "#", ".", "."], 
            [".", "!", "s", ".", ".", ".", "#", ".", ".", "h", ".", ".", ".", "!"],
            ["#", "#", "#", "#", ".", "#", "#", "#", "#", ".", ".", ".", "g", "#"],
            ["!", "!", "!", "#", ".", "h", ".", ".", "#", ".", "!", ".", "#", "."],
            ["#", "#", ".", "#", "#", "!", ".", "#", "#", "#", ".", ".", "#", "."],
            ["!", ".", "h", ".", "#", "#", "!", ".", "#", ".", ".", "d", ".", "#"],
            [".", ".", ".", ".", "#", "#", ".", ".", ".", ".", ".", "h", ".", "."],
            [".", "a", ".", "!", "#", ".", ".", "!", ".", ".", "!", ".", "#", "."],
            ["#", ".", ".", ".", ".", ".", ".", ".", "h", "!", ".", ".", "#", "."],
            ["#", "#", "#", ".", "#", ".", ".", "!", ".", ".", ".", "#", "#", "."],
            ["b", ".", ".", "!", "#", "h", ".", ".", "#", ".", ".", "#", "B", "."]
        ]

        self.player_map = [
            [0] * 14,
            [0] * 14,
            [0] * 14,
            [0] * 14,
            [0] * 14,
            [0] * 14,
            [0] * 14,
            [0] * 14,
            [0] * 14,
            [0] * 14,
            [0] * 14,
        ]
    
    def to_dict(self):
        return {
            "map_data": self.map_data,
            "player_map": self.player_map,
        }

    @classmethod
    def from_dict(cls, data):
        game_map = cls()
        game_map.map_data = data["map_data"]
        game_map.player_map = data["player_map"]
        return game_map

    def display_surroundings(self, player):
        x, y = player.position

        for dy in range(-1, 2):
            print("     ", end="")  

            for dx in range(-1, 2):  
                nx, ny = x + dx, y + dy

                # Vérification des indices pour éviter l'IndexError
                if 0 <= ny < len(self.map_data) and 0 <= nx < len(self.map_data[0]) and 0 <= ny < len(self.player_map) and 0 <= nx < len(self.player_map[0]):
                    if (dx, dy) == (0, 0):
                        print(f"{ORANGE}@{RESET}", end=" ")
                    elif self.player_map[ny][nx] == 1:
                        print(".", end=" ")
                    elif self.map_data[ny][nx] in ("!", "p", "b", "h", "a", "d", "g", "s"):
                        print(f"{LIGHT_BLUE}?{RESET}", end=" ")
                    elif self.map_data[ny][nx] == "#":
                        print(f"{DARK_GREEN}#{RESET}", end=" ")
                    elif self.map_data[ny][nx] == "B":
                        # Boss en rouge
                        print(f"{RED}B{RESET}", end=" ")
                    else:
                        print(".", end=" ")
                else:
                    # Si l'indice est hors de la carte, afficher un mur
                    print(f"{DARK_GREEN}#{RESET}", end=" ")

            print()



    def move_player(self, player, direction):
        x, y = player.position
        system('cls')

        if direction == "north":
            if y - 1 < 0 or self.map_data[y - 1][x] == '#':
                print(f"{DARK_GREEN}You can't go here, the forest is too dense.{RESET}")
            else:
                print(f"{GREY}You move to the North!{RESET}")
                y -= 1

        elif direction == "south":
            if y + 1 >= len(self.map_data) or self.map_data[y + 1][x] == '#':
                print(f"{DARK_GREEN}You can't go here, the forest is too dense.{RESET}")
            else:
                print(f"{GREY}You move to the South!{RESET}")
                y += 1
                print(player.position)

        elif direction == "east":
            if x + 1 >= len(self.map_data[0]) or self.map_data[y][x + 1] == '#':
                print(f"{DARK_GREEN}You can't go here, the forest is too dense.{RESET}")
            else:
                print(f"{GREY}You move to the East!{RESET}")
                x += 1

        elif direction == "west":
            if x - 1 < 0 or self.map_data[y][x - 1] == '#':
                print(f"{DARK_GREEN}You can't go here, the forest is too dense.{RESET}")
            else:
                print(f"{GREY}You move to the West!{RESET}")
                x -= 1

        if self.map_data[y][x] == "b" and self.player_map[y][x] == 0:  
            player.weapon = Weapon("Katana", 1.5) 
            print(f"{GREY}You found a {GRAY_BLUE}Katana{GREY}, The Best Blade !")

        elif self.map_data[y][x] == "g" and self.player_map[y][x] == 0:  
            weapon = ("Great Sword", 1.25) 
            if player.weapon.damage < weapon[1]:
                player.weapon = Weapon("Great Sword", 1.25) 
                print(f"{GREY}You found a {GRAY_BLUE}Great Sword{GREY}. This weapon is better than your {GRAY_BLUE}'{player.weapon.name}'{GREY}, so you equip it!")
            else:
                print(f"{GREY}You found a {GRAY_BLUE}Great Sword{GREY}, but your {GRAY_BLUE}'{player.weapon.name}'{GREY} is better, so you continue using it.")

        elif self.map_data[y][x] == "s" and self.player_map[y][x] == 0:  
            weapon = ("Sword", 1) 
            if player.weapon.damage < weapon[1]:
                player.weapon = Weapon("Sword", 1) 
                print(f"{GREY}You found a {GRAY_BLUE}Sword{GREY}. This weapon is better than your {GRAY_BLUE}'{player.weapon.name}'{GREY}, so you equip it!")
            else:
                print(f"{GREY}You found a {GRAY_BLUE}Sword{GREY}, but your {GRAY_BLUE}'{player.weapon.name}'{GREY} is better, so you continue using it.")

        elif self.map_data[y][x] == "!" and self.player_map[y][x] == 0: 
            monster = Monster(player.level +1)  
            combat = Combat(player, monster)
            combat.start()

        elif self.map_data[y][x] == "h" and self.player_map[y][x] == 0: 
            player.inventory.healpotion += 1
            print(f"{GREY}You found a {DARK_GREEN}heal potion{GREY}! You can use it to {DARK_GREEN}heal{GREY} yourself.")

        elif self.map_data[y][x] == "a" and self.player_map[y][x] == 0:
            player.inventory.attackpotion += 1
            print(f"{GREY}You found an {BROWN}Attack Potion{GREY}! You can use it to {BROWN}boost your attack{GREY} in combat.")

        elif self.map_data[y][x] == "d" and self.player_map[y][x] == 0:
            player.inventory.defensepotion += 1
            print(f"{GREY}You found a {LIGHT_BLUE}Defense Potion{GREY}! You can use it to {LIGHT_BLUE}increase your defense{GREY} in combat.")

        elif self.map_data[y][x] == "B" : 
            boss = Monster(player.level + 5,True)  
            combat = Combat(player, boss)
            print("A boss has appeared! Prepare yourself for a tough battle!")
            combat.start()

        self.player_map[y][x] = 1

        player.position = (x, y)

