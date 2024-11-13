from game.menu import show_mainmenu, show_aboutmenu
from game.game_manager import GameManager
from os import system
from data.save import Load

# Codes de couleur ANSI
RESET = "\033[0m"
GREEN = "\033[92m"

def main():
    game = GameManager()
    system('cls')
    while game.running:
        show_mainmenu()
        choice = input(f"{GREEN}>{RESET} ")


        if choice == "1":
            game.start_new_game()
        elif choice == "2":
            game.load_saved_game()
        elif choice == "3":
            show_aboutmenu()
        elif choice == "4":
            game.exit_game()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
