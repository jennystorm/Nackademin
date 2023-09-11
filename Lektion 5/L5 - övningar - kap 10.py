kosmetika = 30

# Övningsuppgift 10.1
# Vägskylt vars meddelande finns lagrat i en textfil

import os
"""
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
# Beräkna förekomsten av heltal i en excel-fil

print("*" * kosmetika)
print("Antal gånger siffran förekommer i en fil.")
print("*" * kosmetika)

with open("numbers.csv", "r") as f:
    numbers = f.read()
numbers = numbers.split()

number0 = 0
number1 = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0
number6 = 0
number7 = 0
number8 = 0
number9 = 0

for i in numbers:
    if i == "0":
        number0 += 1
    elif i == "1":
        number1 += 1
    elif i == "2":
        number2 += 1
    elif i == "3":
        number3 += 1
    elif i == "4":
        number4 += 1
    elif i == "5":
        number5 += 1
    elif i == "6":
        number6 += 1
    elif i == "7":
        number7 += 1
    elif i == "8":
        number8 += 1
    elif i == "9":
        number9 += 1
    else:
        print("Något gick på tok")
        break

print ("---------------")
print ("- NUMANALYZER -")
print ("---------------")
print ("| 0 |\t", number0)
print ("| 1 |\t", number1)
print ("| 2 |\t", number2)
print ("| 3 |\t", number3)
print ("| 4 |\t", number4)
print ("| 5 |\t", number5)
print ("| 6 |\t", number6)
print ("| 7 |\t", number7)
print ("| 8 |\t", number8)
print ("| 9 |\t", number9)
"""

# Övningsuppgift 10.3
import json

counter = 0

while True:
    counter = 0
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    print("*" * kosmetika)
    print("Sökbar databas med personuppgifter.")
    print("*" * kosmetika, "\n")
    print(".: PEOPLES DATABASE :.")
    print("----------------------")
    print("get_id | Get person by ID")
    print("scan_f | List people by FORENAME")
    print("scan_s | List people by SURNAME")
    print("exit   | Exit program")
    print("----------------------")
    with open("database.csv", "r", encoding= "utf-8") as f:
        database = f.read()
    database = database.split()
    command = input("Menu > ")
    if command == "get_id":
        try:
            command = int(input("ID > "))
            command += 1
            person = database[command].split(",")
            print("| ID:\t\t", person[0])
            print("| FORNAME:\t", person[1])
            print("| SURNAME:\t", person[2])
            print("| GENDER:\t", person[3])
            print("| YEAR:\t\t", person[4])
            command = input("Press enter to continue > ")
        except:
            print ("ID has to be entered with numbers.")
            command = input("Press enter to start over. > ")
    elif command == "scan_f":
        command = input("FORENAME > ")
        command = command.capitalize()
        for i in database:
            forename = i.split(",")
            if forename[1] == command:
                print (i)
                counter += 1
        if counter == 0:
            print("No persons with that forename found.")
        command = input("Press enter to start over. > ")
    elif command == "scan_s":
        command = input("SURNAME > ")
        command.capitalize()
        for i in database:
            surname = i.split(",")
            if surname[2] == command:
                print (i)
                counter += 1
        if counter == 0:
            print("No persons with that surname found.")
        command = input("Press enter to start over. > ")
    elif command == "exit":
        print("Exit program.")
        break
    else:
        print("Unknown command.")
        command = input("Press enter to start over. > ")