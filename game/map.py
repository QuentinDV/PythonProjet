from game.monster import Monster  
from game.combat import Combat
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
            ["@", "#", "!", ".", "hp", "#", ".", "b"], 
            [".", "!", ".", "#", ".", "!", "hp", "#"],
            ["#", "#", ".", "#", "#", "#", "#", "#"], 
            ["#", ".", ".", "#", ".", ".", ".", "#"],
            ["#", ".", "#", "#", ".", "#", ".", "#"],
            ["#", "!", "hp", ".", "!", "#", "B", "#"],
        ]

        self.player_map = [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]



    def display_surroundings(self, player):
        x, y = player.position

        for dy in range(-1, 2):
            print("     ", end="")  

            for dx in range(-1, 2):  
                nx, ny = x + dx, y + dy

                if ny < 0 or ny >= len(self.map_data) or nx < 0 or nx >= len(self.map_data[0]):
                    print(f"{DARK_GREEN}#{RESET}", end=" ")
                elif (dx, dy) == (0, 0):
                    print(f"{ORANGE}@{RESET}", end=" ")
                elif self.player_map[ny][nx] == 1:
                    print(".", end=" ")
                elif self.map_data[ny][nx] in ("!", "p", "b", "hp", "ap", "dp", "gs", "sw"):
                    print(f"{LIGHT_BLUE}?{RESET}", end=" ")
                elif self.map_data[ny][nx] == "#":
                    print(f"{DARK_GREEN}#{RESET}", end=" ")
                else:
                    print(".", end=" ")

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
            player.weapon = ("Katana", 1.5) 
            print(f"{GREY}You found a {GRAY_BLUE}Katana{GREY}, The Best Blade !")

        elif self.map_data[y][x] == "gs" and self.player_map[y][x] == 0:  
            weapon = ("Great Sword", 1.25) 
            if player.weapon[1] < weapon[1]:
                player.weapon = ("Great Sword", 1.25) 
                print(f"{GREY}You found a {GRAY_BLUE}Great Sword{GREY}. This weapon is better than your {GRAY_BLUE}'{player.weapon[0]}'{GREY}, so you equip it!")
            else:
                print(f"{GREY}You found a {GRAY_BLUE}Great Sword{GREY}, but your {GRAY_BLUE}'{player.weapon[0]}'{GREY} is better, so you continue using it.")

        elif self.map_data[y][x] == "sw" and self.player_map[y][x] == 0:  
            weapon = ("Sword", 1) 
            if player.weapon[1] < weapon[1]:
                player.weapon = ("Sword", 1) 
                print(f"{GREY}You found a {GRAY_BLUE}Sword{GREY}. This weapon is better than your {GRAY_BLUE}'{player.weapon[0]}'{GREY}, so you equip it!")
            else:
                print(f"{GREY}You found a {GRAY_BLUE}Sword{GREY}, but your {GRAY_BLUE}'{player.weapon[0]}'{GREY} is better, so you continue using it.")

        elif self.map_data[y][x] == "!" and self.player_map[y][x] == 0: 
            monster = Monster(player.level +1)  
            combat = Combat(player, monster)
            combat.start()

        elif self.map_data[y][x] == "hp" and self.player_map[y][x] == 0: 
            player.healpotion += 1
            print(f"{GREY}You found a {DARK_GREEN}heal potion{GREY}! You can use it to {DARK_GREEN}heal{GREY} yourself.")

        elif self.map_data[y][x] == "ap" and self.player_map[y][x] == 0:
            player.attackpotion += 1
            print(f"{GREY}You found an {BROWN}Attack Potion{GREY}! You can use it to {BROWN}boost your attack{GREY} in combat.")

        elif self.map_data[y][x] == "dp" and self.player_map[y][x] == 0:
            player.defensepotion += 1
            print(f"{GREY}You found a {LIGHT_BLUE}Defense Potion{GREY}! You can use it to {LIGHT_BLUE}increase your defense{GREY} in combat.")

        elif self.map_data[y][x] == "B" : 
            boss = Monster(player.level + 3)  
            combat = Combat(player, boss)
            print("A boss has appeared! Prepare yourself for a tough battle!")
            combat.start()

        self.player_map[y][x] = 1

        player.position = (x, y)

