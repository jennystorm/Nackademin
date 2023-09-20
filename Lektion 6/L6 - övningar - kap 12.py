kosmetika = 30

# Övningsuppgift 12.1
# Användaren väljer vilken titel som ska skrivas ut genom att mata in dess titel

notes = {
"Meddelande från skolan": "Friluftsdag på tisdag",
"Kom ihåg!": "Ta bilen till verkstad",
"Inför tentamen ": "Gör alla instuderingsuppgifter"
}
"""
print("*"*kosmetika)
print(("Övning 12.1").center(kosmetika))
print("*"*kosmetika, "\n")
while True:
    command = input("Anteckning >")
    try:
        print("-"*kosmetika)
        print(notes[command])
        print("-"*kosmetika)
        break
    except:
        print("FEL. Anteckningen finns inte.")



# Övningsuppgift 12.2
# Iterera genom listan med en for-loop
print("\n")
print("*"*kosmetika)
print(("Övning 12.2").center(kosmetika))
print("*"*kosmetika, "\n")
print("-"*kosmetika)
print((". : Anteckningar : .").center(kosmetika))
print("-"*kosmetika)
for i in notes:
    print (i)

# Övningsuppgift 12.3
# Genom iteration skriva ut både titel och text

print("\n")
print("*"*kosmetika)
print(("Övning 12.3").center(kosmetika))
print("*"*kosmetika, "\n")
for i in notes:
    print ("-"*kosmetika)
    print("Titel:", i)
    print("Text:", notes[i])


# Övningsuppgift 12.4
# Låt en användare lägga till eller ändra en anteckning genom att mata in titel och text

print("\n")
print("*"*kosmetika)
print(("Övning 12.4").center(kosmetika))
print("*"*kosmetika, "\n")


print("Lägg till artikel:")
titel = input("Titel > ")
text = input("Text > ")
notes.update({titel:text})

for i in notes:
    print ("-"*kosmetika)
    print("Titel:", i)
    print("Text:", notes[i])


# Övningsuppgift 12.5
# Låt användaren ta bort en titel

print("\n")
print("*"*kosmetika)
print(("Övning 12.5").center(kosmetika))
print("*"*kosmetika, "\n")

print("Ta bort artikel:")
titel = input("Titel > ")
notes.pop(titel)

for i in notes:
    print ("-"*kosmetika)
    print("Titel:", i)
    print("Text:", notes[i])

"""

# Övningsuppgift 12.6
# Fullständigt program där användaren kan lista, visa, skapa, ändra och ta bort anteckningar

import json


print("\n")
print("*"*kosmetika)
print(("Övning 12.6").center(kosmetika))
print("*"*kosmetika, "\n")


while True:
    with open("notes.json", "r") as f:
        notes = f.read()
    notes = json.loads(notes)
    while True:
        print("*" * kosmetika)
        print("Redigerbar anteckningsbok.")
        print("*" * kosmetika, "\n")
        print(".: ALWAYSNOTE :.")
        print("----------------------")
        if len(notes) == 0:
            print ("Empty.")
        else:
            for i in notes:
                print (i)
        print("----------------------")
        print("view | view note")
        print("add | add note")
        print("rm | remove note")
        print("exit | exit program")
        print("----------------------")
        command = input("Menu > ")
        command = command.lower()
        # Save changes and exit program
        if command == "exit":
            with open("notes.json", "w") as f:
                notes = json.dumps(notes)
                f.write(notes)
            break
        # View specific note
        elif command == "view":
            command = input("Title: ")
            command = command.capitalize()
            try:
                print(notes[command])
                command = input("Press enter to continue...")
            except:
                print("Title not found.")
                command = input("Press enter to continue...")
        # Remove note/item
        elif command == "rm":
            counter = 0
            command = input("Title > ")
            command = command.capitalize()
            for note in notes:
                if note == command:
                    counter += 1
                    print(F"This will delete '{note}: {notes[command]}'.")
                    command_2 = input("Do you wish to continue? Y/N >")
                    command_2 = command_2.capitalize()
                    if command_2 == "Y":
                        del notes[command]
                        print("The item have been removed.")
                        command_2 = input("Press enter to continue...")
                        break
                    elif command_2 == "N":
                        print("The item have not been removed.")
                        command_2 = input("Press enter to continue...")
                    else:
                        print("Unknown command.")
                        command_2 = input("Press enter to continue...")
            if counter == 0:
                print("Item not found.")
                command_2 = input("Press enter to continue...")
            else:
                continue
        # Add/change note/item
        elif command == "add":
            counter = 0
            command = input("Title > ")
            command = command.capitalize()
            for note in notes:
                if note == command:
                    counter += 1
                    print("There is already a note with this title.\nProceeding will overwrite that note.")
                    command_2 = input("Do you wish to proceed? Y/N > ")
                    command_2 = command_2.capitalize()
                    if command_2 == "Y":
                        counter = 0
                    elif command_2 == "N":
                        print("The item has not been overwritten.")
                        command_2 = input("Press enter to continue...")
                    else:
                        print("Unknown command.")
                        command_2 = input("Press enter to continue...")
            if counter == 0:
                print(F"Enter the text/message you want connected to the title {command}")
                command_2 = input("> ")
                notes[command] = command_2
            else:
                continue
        else:
            print("UNKNOWN COMMAND.")
            command = input("Press enter to continue...")
    # End program completely
    print("The notes have been saved in the file 'notes.json'.")
    command = input("Enter 0 to exit completely or enter to restart the program.\n > ")
    if command == "0":
        break
    else:
        continue
