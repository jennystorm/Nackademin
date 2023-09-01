# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 14:22:20 2023

@author: jenny
"""

# Övningsuppgifft 3.1

x = int(input("Ange ett heltal: "))
y = int(input("Ange ytterligare ett heltal: "))
z = int(input("Ange ett sista heltal: "))

if x > y and x > z:
    print("Det största inmatade talet är", x)
elif y > x and y > z:
    print("Det största inmatade talet är", y)
else:
    print("Det största inmatade talet är", z)


# Övningsuppgift 3.2

namn = input("Ange ditt namn: ")
alder = int(input("Ange din ålder: "))

if alder < 2:
    print(f"Hej {namn}! Enligt vårdguidens rekommendationer behöver individer i din ålder ({alder} år) sova minst 14 timmar per natt.")
elif alder < 3:
    print("Hej", namn + "!", "Enligt vårdguidens rekommendationer behöver individer i din ålder (" + str(alder), "år) sova minst 13 timmar per natt.")
elif alder < 4:
    print("Hej", namn + "!", "Enligt vårdguidens rekommendationer behöver individer i din ålder (" + str(alder), "år) sova minst 12 timmar per natt.")
elif alder < 5:
    print("Hej", namn + "!", "Enligt vårdguidens rekommendationer behöver individer i din ålder (" + str(alder), "år) sova minst 11,5 timmar per natt.")
elif alder < 7:
    print("Hej", namn + "!", "Enligt vårdguidens rekommendationer behöver individer i din ålder (" + str(alder), "år) sova minst 11 timmar per natt.")
elif alder < 8:
    print("Hej", namn + "!", "Enligt vårdguidens rekommendationer behöver individer i din ålder (" + str(alder), "år) sova minst 10,5 timmar per natt.")
elif alder < 11:
    print("Hej", namn + "!", "Enligt vårdguidens rekommendationer behöver individer i din ålder (" + str(alder), "år) sova minst 10 timmar per natt.")
elif alder < 12:
    print("Hej", namn + "!", "Enligt vårdguidens rekommendationer behöver individer i din ålder (" + str(alder), "år) sova minst 9,5 timmar per natt.")
elif alder < 16: 
    print("Hej", namn + "!", "Enligt vårdguidens rekommendationer behöver individer i din ålder (" + str(alder), "år) sova minst 9 timmar per natt.")
elif alder < 17:
    print("Hej", namn + "!", "Enligt vårdguidens rekommendationer behöver individer i din ålder (" + str(alder), "år) sova minst 8,5 timmar per natt.")
else:
    print("Hej", namn + "!", "Enligt vårdguidens rekommendationer behöver individer i din ålder (" + str(alder), "år) sova minst 8 timmar per natt.")


#  Övningsuppgift 3.3

import random

dice = random.randint(1, 6)

print ("Du slog en", str(dice) + ":a!")

if dice == 1:
    print (""" 
----------
|        |
|   X    |
|        |
----------""")
elif dice == 2:
    print ( """
----------
|   X    |
|        |
|   X    |
----------""")
elif dice == 3:
    print ("""
----------
| X      |
|   X    |
|     X  |
----------""")
elif dice == 4:
    print ("""
----------
| X    X |
|        |
| X   X  |
----------""")
elif dice == 5:
    print ("""
----------
| X    X |
|   X    |
| X   X  |
----------""")
elif dice == 6:
    print ("""
----------
| X    X |
| X    X |
| X    X |
----------""")


# Övningsuppgift 3.4 

country = input("Skriv ett land som tillhör Norden eller Storbrittanien: ")

if country.casefold() == "danmark" or country.casefold() == "finland" or country.casefold() == "island" or country.casefold() =="sverige":
    print (country.capitalize(), "tillhör Norden.")
elif country.casefold() == "england" or country.casefold() == "nordirland" or country.casefold() == "skottland" or country.casefold() == "wales":
    print (country.capitalize(), "tillhör Storbrittanien.")
else:
    print (country.capitalize(), "tillhör varken Norden eller Storbrittanien.")


# Övningsuppgift 3.5

gender = input("Skriv in kön: (man/kvinna)")
hair_colour = input("Skriv in hårfärg: (brun/röd)")
eye_colour = input("Skriv in ögonfärg: (brun/blå)")

if gender == "man":
    if hair_colour == "brun":
        if eye_colour == "brun":
            print ("Egenskaperna matchar Daniel Radcliffe.")
        elif eye_colour == "blå":
            print ("Egenskaperna matchar Rasmus på Luffen.")
    elif hair_colour == "röd":
        if eye_colour == "brun":
            print ("Egenskaperna matchar Reynald Räv.")
        elif eye_colour == "blå":
            print ("Egenskaperna matchar Rupert Grint.")
elif gender == "kvinna":
    if hair_colour == "brun":
        if eye_colour == "brun":
            print ("Egenskaperna matchar Emma Watson och Selena Gomez.")
        elif eye_colour == "blå":
            print ("Egenskaperna matchar Jenny Storm.")
    elif hair_colour == "röd":
        if eye_colour == "brun":
            print ("Egenskaperna matchar Flickan med det röda håret.")
        elif eye_colour == "blå":
            print ("Egenskaperna matchar Pippi Långstrump.")
else:
    print ("Egenskaperna matchar ingen.")
    

# Övningsuppgift 4.1

lista = []
summa = 0
x = 0

while True:
    x = int(input("Skriv in ett tal:"))
    if x >= 0:
        lista.append(x)
    elif x < 0:
        break

for i in lista:
    summa += i
    
print ("Minsta tal:", min(lista))
print ("Största tal:", max(lista))
print ("Summa:", summa)
print ("Medelvärde:", summa/len(lista))

# Övningsuppgift 4.2

tabell = int(input("Ange en multiplikationstabell:"))
counter = 0

for i in range (0, 101, tabell):
    if counter == 0:
        counter += 1
    elif counter > 0 and counter < 4:
        print (i)
        counter += 1
    elif counter == 4:
        svar = input("Vill du avsluta? y/n ")
        if svar == "y":
            break 
        elif svar == "n":
            counter = 1
            
# Övningsuppgift 4.3

answer = random.randint(0, 99)
counter = 0

print ("----------")
print ('Välkommen till spelet "Högre eller lägre"!')
print ("Datorn kommer att generera ett tal mellan 0-99, kan du gissa vilket?")
print ("----------")

while True:
    guess = int(input("Vad gissar du? "))
    counter += 1
    if guess == answer:
        print("----------")
        print (f"{guess} är korrekt!")
        print (f"Det tog dig {counter} gissningar.")
        print ("Bra jobbat!")
        break
    elif guess < answer:
        print ("Högre!")
    elif guess > answer:
        print ("Lägre!")