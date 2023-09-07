# Övningsuppgift 5.1

tal = input("Skriv in ett heltal:")

try:
    tal = int(tal)
    print(tal * 2)
except ValueError:
    print(tal, "är inte heltal skrivet med siffror")

# Övningsuppgift 5.2


while True:
    try:
        taljare = float(input("Skriv täljaren: "))
        break
    except:
        print("Ogiltigt nummer. Skriv med siffror")

while True:
    try:
        namnare = float(input("Skriv nämnaren: "))
        if namnare == 0:
            print("Nämnaren får inte vara 0.")
        else:
            break
    except:
        print("Ogiltigt nummer. Skriv med siffror")

print(taljare / namnare)

# Övningsuppgift 5.3

kosmetika = 35
print ("*" * kosmetika)
print ("Mata in ett valfritt antal tal \nför att räkna ut kardinalitet, \nsumma och medelvärde.")
print ("*" * kosmetika)

nummerlista = []
summa = 0

while True:
    nummer = input("Skriv ett tal med siffror eller avsluta inmatning med exit: ")
    try:
        if nummer == "exit":
            break
        else:
            nummer = float(nummer)
            nummerlista.append(nummer)
            print (nummerlista)
    except:
        print ("-" * kosmetika)
        print("Felinmatning. Mata in talet med siffror. \nEx. 5 eller 2,45")
        print ("-" * kosmetika)


for i in nummerlista:
    summa += i

print ("*" * kosmetika)
print ("Kardinalitet:\t",(len(nummerlista)))
print ("Summa:\t\t\t", summa)
print ("Medelvärde:\t\t", summa/(len(nummerlista)))
print ("*" * kosmetika)

