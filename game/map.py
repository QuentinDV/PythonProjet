class GameMap:
    def __init__(self):
        # Carte sous forme de matrice 2D
        self.map_data = [
            ["#", "#", ".", ".", ".", "#"],  # 0,0 -> Starting point (forest), 0,1 -> dense thicket
            [".", ".", "@", ".", ".", "."],  # 1,0 -> Quiet glade, 1,1 -> Boss lair
            ["#", ".", ".", ".", ".", "#"],  # 2,0 -> More trees, 2,1 -> Boss area
        ]

    def describe_map(self, player_position):
        # Affichage de la carte avec couleurs
        for y, row in enumerate(self.map_data):
            for x, cell in enumerate(row):
                if (x, y) == player_position:
                    print("\033[33m@", end=" ")  # Le joueur en orange
                elif cell == "#":
                    print("\033[32m#", end=" ")  # Arbres en vert
                else:
                    print(".", end=" ")  # Autres espaces
            print()  # Nouvelle ligne pour la ligne suivante

    def move_player(self, player, direction):
        x, y = player.position
        if direction == "north" or direction == "n":
            y -= 1
        elif direction == "south" or direction == "s":
            y += 1
        elif direction == "east" or direction == "e":
            x += 1
        elif direction == "west" or direction == "w":
            x -= 1
        player.position = (x, y)
