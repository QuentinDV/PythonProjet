from game.map import GameMap
from time import sleep
def show_mainmenu():
    print("\033[91mThis game needs to be played with a terminal window height of at least 10 lines.\033[0m")
    print("""
\033[38;5;214mMAIN MENU\033[0m
1. Create New Game
2. Load Saved Game
3. About
4. Exit
          """)

def show_aboutmenu():
    print("\033[38;5;220mThis is a simple game created using Python made by Quentin Dassi Vignon\033[0m")


def tutorial():
    print("""Keybinds :
Go Top/North : Z, N or T 
Go Bottom/South : S
Go Left/West : L, Q or W 
Go Right/East : R, D or E
Open Inventory : I
See Keybinds : K
Type "SAVE" to save your progress 
Type "Exit" to left the game without saving""")

def display_health(player):
    max_hp = player.max_hp
    current_hp = player.hp

    full_blocks = current_hp // 10
    empty_blocks = (max_hp // 10) - full_blocks

    health_bar = "▮" * full_blocks + "▯" * empty_blocks

    return f"HP: [{health_bar} ] {current_hp}/{max_hp}"


def win_menu():
    print("\033[92m" + """
____    ____  ______    __    __     ____    __    ____  __  .__   __. 
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | 
  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | 
    |__|     \______/   \______/         \__/  \__/     |__| |__| \__| """ + "\033[0m")

def loose_menu():
    print("\033[91m" + """
____    ____  ______    __    __      __        ______     ______        _______. _______ 
\   \  /   / /  __  \  |  |  |  |    |  |      /  __  \   /  __  \      /       ||   ____|
 \   \/   / |  |  |  | |  |  |  |    |  |     |  |  |  | |  |  |  |    |   (----`|  |__   
  \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  | |  |  |  |     \   \    |   __|  
    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | |  `--'  | .----)   |   |  |____ 
    |__|     \______/   \______/     |_______| \______/   \______/  |_______/    |_______|
\033[0m""")
    sleep(3)