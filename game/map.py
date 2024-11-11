from game.monster import Monster  
from game.combat import Combat
from os import system

class GameMap:
    def __init__(self):
        self.map_data = [
            ["@", "#", "!", ".", "p", "#", ".", "b"], 
            [".", "!", ".", "#", ".", "!", "p", "#"],
            ["#", "#", ".", "#", "#", "#", "#", "#"], 
            ["#", ".", ".", "#", ".", ".", ".", "#"],
            ["#", ".", "#", "#", ".", "#", ".", "#"],
            ["#", "!", "p", ".", "!", "#", "B", "#"],
        ]

    def display_surroundings(self, player):
        x, y = player.position

        for dy in range(-1, 2):
            print("     ", end="")  

            for dx in range(-1, 2):  
                nx, ny = x + dx, y + dy

                if ny < 0 or ny >= len(self.map_data) or nx < 0 or nx >= len(self.map_data[0]):
                    print("\033[32m#\033[0m", end=" ")  
                elif (dx, dy) == (0, 0):
                    print("\033[33m@\033[0m", end=" ")  
                elif self.map_data[ny][nx] in ("!", "p", "b"):
                    print("?", end=" ")  
                elif self.map_data[ny][nx] == "#":
                    print("\033[32m#\033[0m", end=" ")  
                else:
                    print(".", end=" ")  
            print()  

    def move_player(self, player, direction):
        x, y = player.position
        system('cls')

        if direction == "north":
            if y - 1 < 0 or self.map_data[y - 1][x] == '#':
                print("\033[92mYou can't go here, the forest is too dense.\033[0m ")
            else:
                print("\033[33mYou move to the North!\033[0m")
                y -= 1

        elif direction == "south":
            if y + 1 >= len(self.map_data) or self.map_data[y + 1][x] == '#':
                print("\033[92mYou can't go here, the forest is too dense.\033[0m ")
            else:
                print("\033[33mYou move to the South!\033[0m")
                y += 1

        elif direction == "east":
            if x + 1 >= len(self.map_data[0]) or self.map_data[y][x + 1] == '#':
                print("\033[92mYou can't go here, the forest is too dense.\033[0m ")
            else:
                print("\033[33mYou move to the East!\033[0m")
                x += 1

        elif direction == "west":
            if x - 1 < 0 or self.map_data[y][x - 1] == '#':
                print("\033[92mYou can't go here, the forest is too dense.\033[0m ")
            else:
                print("\033[33mYou move to the West!\033[0m")
                x -= 1

        if self.map_data[y][x] == "b":  
            player.weapon = ("Katana", 2) 
            print("You found a Katana! It doubles your damage!")

        elif self.map_data[y][x] == "!": 
            monster_level = max(player.level - 1, 1) 
            monster = Monster(monster_level)  
            combat = Combat(player, monster)
            combat.start()

        elif self.map_data[y][x] == "p": 
            player.healpotion += 1
            print("You found a potion! You can use it to heal yourself.")

        elif self.map_data[y][x] == "B": 
            boss = Monster(player.level + 3)  
            combat = Combat(player, boss)
            print("A boss has appeared! Prepare yourself for a tough battle!")
            combat.start()

        player.position = (x, y)

