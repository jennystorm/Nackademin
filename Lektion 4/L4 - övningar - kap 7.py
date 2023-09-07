# Övningsuppgift 7.1

POST_1 = ""
POST_2 = ""
POST_3 = ""

import os

while True :
    # 1. Rensa terminalfönster
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    # 2. Skriv ut instruktioner
    print (".: basicBILLBOARD :. ")
    print (" ******************** ")
    print ("P1:", POST_1)
    print ("P2:", POST_2)
    print ("P3:", POST_3)
    print (" --------------------")
    print ("c | Ändra post ")
    print ("e | Stäng program ")
    print (" --------------------")

    # 3. Hämta kommando från användaren
    val = input("Vad vill du göra?")
    # 4. Utför operationer för inmatat kommando
    if val == "e":
        break
    elif val == "c":
        nyttval = input("Vilken post vill du ändra? 1, 2 eller 3?")
        if nyttval == "1":
            POST_1 = input("Skriv nytt meddelande för post 1:")
        elif nyttval == "2":
            POST_2 = input("Skriv nytt meddelande för post 2:")
        elif nyttval == "3":
            POST_3 = input("Skriv nytt meddelande för post 3:")
        else:
            print("Felaktigt kommando.")
    else:
        print("Felaktigt kommando.")
    # 5. Pausa exekvering
    input ("Tryck enter för att fortsätta ... ")
    # 6. Gå till 1
