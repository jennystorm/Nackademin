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

"""

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



# Övningsuppgift 12.6
# Fullständigt program där användaren kan lista, visa, skapa, ändra och ta bort anteckningar

print("\n")
print("*"*kosmetika)
print(("Övning 12.6").center(kosmetika))
print("*"*kosmetika, "\n")

