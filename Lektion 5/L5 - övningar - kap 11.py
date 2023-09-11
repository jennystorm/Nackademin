kosmetika = 30
import json


# Övningsuppgift 11.1
# Omvandla listan till JSON och skriv därefter ut den på skärmen
random_stuff = [1337, 13.37, "Ååh Yää!"]
print(random_stuff)
random_stuff = json.dumps(random_stuff)
print(random_stuff)

# Övningsuppgift 11.2
# Omvandla JSON-objekt till lista i Python, skriv ut genom att iterera
my_chars = '["abc","\u00e5\u00e4\u00f6","123"]'
print(my_chars)
my_chars = json.loads(my_chars)
for i in my_chars:
    print (i)

# Övningsuppgift 11.3
# Konstruera ett script där användare matar in en serie heltal. Heltalen + summa ska presenteras för användaren.

numbers = []
counter = 0
summa = 0

while True:
    with open("heltal.json", "r") as f:
        numbers = f.read()
    numbers = json.loads(numbers)
    while True:
        print("*" * kosmetika)
        print("Sökbar databas med personuppgifter.")
        print("*" * kosmetika, "\n")
        print(".: intMEMORIZER :.")
        print("----------------------")
        summa = 0
        for i in numbers:
            print("*", i)
            summa += i
        print("----------------------")
        print("SUMMA:", summa)
        print("----------------------")
        print("mata in heltal")
        print("0 stänger scriptet")
        print("----------------------")
        try:
            heltal = int(input("Mata in heltal > "))
            if heltal == 0:
                with open("heltal.json", "w") as f:
                    numbers = json.dumps(numbers)
                    f.write(numbers)
                break
            else:
                for i in numbers:
                    if i == heltal:
                        counter += 1
                if counter == 0:
                    numbers.append(heltal)
                else:
                    counter = 0
        except:
            print("FEL: Ogiltigt heltal")
            command = input("Tryck enter för att fortsätta...")
    print("Heltalen har sparats i filen 'heltal.json'.")
    command = input("Tryck 0 för att avsluta helt eller enter för att fortsätta. > ")
    if command == "0":
        break
    else:
        continue








