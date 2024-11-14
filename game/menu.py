from game.map import GameMap
from time import sleep

# Codes de couleur ANSI
RESET = "\033[0m"
DARK_GREEN = "\033[38;5;22m"
ORANGE = "\033[38;5;214m"
RED = "\033[91m"
GREEN = "\033[92m"
GREY = "\033[38;5;245m"

# Affichage du menu principal
def show_mainmenu():
    print("")
    print(f"{RED}This game needs to be played with a terminal window height of at least 10 lines.{RESET}")
    print(f"""
{ORANGE}MAIN MENU{RESET}
{GREEN}1{RESET}. Create New Game
{GREEN}2{RESET}. Load Saved Game
{GREEN}3{RESET}. About
{GREEN}4{RESET}. Exit
          """)
    
# Affichage du menu de credit
def show_aboutmenu():
    print("\033[38;5;220mThis is a simple game created using Python made by Quentin Dassi Vignon\033[0m")

# Affichage des touches
def tutorial():
    print(f"""{DARK_GREEN}Keybinds:{RESET}
{GREY}Go Top/North:{RESET} Z, N or T 
{GREY}Go Bottom/South:{RESET} S, B
{GREY}Go Left/West:{RESET} L, Q or W 
{GREY}Go Right/East:{RESET} R, D or E
{GREY}Open Inventory:{RESET} I
{GREY}See Keybinds:{RESET} H
{ORANGE}Type "Save" to save your progress{RESET}
{ORANGE}Type "Exit" to left the game without saving{RESET}""")

# affichage de la vie du joueur
def display_health(player):
    max_hp = player.max_hp
    current_hp = player.hp

    full_blocks = current_hp // 10
    empty_blocks = (max_hp // 10) - full_blocks

    health_bar = "▮" * full_blocks + "▯" * empty_blocks

    return f"{GREEN}HP:{RESET} [{health_bar} ] {current_hp}/{max_hp}"

# Affichage du menu de victoire
def win_menu():
    print(f"""{GREEN}
____    ____  ______    __    __     ____    __    ____  __  .__   __. 
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | 
  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | 
    |__|     \______/   \______/         \__/  \__/     |__| |__| \__| {RESET}""")
    sleep(3)

# Affichage du menu de défaite
def loose_menu():
    print(f"""{RED}
____    ____  ______    __    __      __        ______     ______        _______. _______ 
\   \  /   / /  __  \  |  |  |  |    |  |      /  __  \   /  __  \      /       ||   ____|
 \   \/   / |  |  |  | |  |  |  |    |  |     |  |  |  | |  |  |  |    |   (----`|  |__   
  \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  | |  |  |  |     \   \    |   __|  
    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | |  `--'  | .----)   |   |  |____ 
    |__|     \______/   \______/     |_______| \______/   \______/  |_______/    |_______|
{RESET}""")
    sleep(3)