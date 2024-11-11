from game.menu import show_mainmenu, show_aboutmenu
from game.game_manager import GameManager


def main():
    game = GameManager()
    while game.running:
        show_mainmenu()
        choice = input("\033[92m>\033[0m ")

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
