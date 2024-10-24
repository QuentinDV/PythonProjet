from menus.main import *
Running = True

def mainmenu():
    global Running
    
    show_mainmenu()
    choice = input((">"))

    if choice == "4":
        print("Exiting...")
        Running = False

    elif choice == "3":
        show_aboutmenu()

    elif choice == "2":
        print("""Loading... 
1001 Errors""")
        Running = False

    elif choice == "1":
        print("""Loading... 
1001 Errors""")
        Running = False

    else:
        print("Invalid choice, please try again.")
        


while Running :
    mainmenu()