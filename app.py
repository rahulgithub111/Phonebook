from src.GenerateSecret import GenerateSecret
from src.Exit import Exit
from src.NotFound import NotFound
from src.PhoneBook import PhoneBook

class Main:
    def __init__(self):
        print("Welcome Back !")
        print("App Menu")
        print("1. Generate Secret")
        print("2. PhoneBook")
        print("3. Exit")
        option=int(input("Choose an option:\n"))
        if option == 1: 
            GenerateSecret()
            Main()
        elif option == 2 : 
            PhoneBook()
            Main()   
        elif option == 3: Exit()
        else: 
            NotFound()
            Main()

Main()