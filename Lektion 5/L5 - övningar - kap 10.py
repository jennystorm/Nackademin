kosmetika = 30

# Övningsuppgift 10.1
# Vägskylt vars meddelande finns lagrat i en textfil

import os

while True:
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    print("*" * kosmetika)
    print("Vägskylt vars meddelande finns lagrat i en textfil")
    print("*" * kosmetika, "\n")
    with open("sign.txt", "r") as f:
        sign = f.read()
    print("| - - - - - - - - - - - - - - - - |")
    print("| ### ----------------------- ### |")
    print("| ### | ", sign.center(17) , " | ### |")
    print("| ### ----------------------- ### |")
    print("| - - - - - - - - - - - - - - - - |")
    print("| C | Change sign message")
    print("| E | Exit program")
    print("| - - - - - - - - - - - - - - - - |")
    command = input("Meny > ")
    if command == "C":
        print ("Meddelandet får ej vara längre än 15 tecken.")
        command = input("Meny > ")
        if len(command) <= 15:
            with open("sign.txt", "w") as f:
                f.write(command)
        else:
            print("Meddelandet är för långt.")
            command = input("Tryck enter för att börja om.")
    elif command == "E":
        print ("Programmet avslutat.")
        print ("*"*kosmetika, "\n\n")
        break

# Övningsuppgift 10.2

