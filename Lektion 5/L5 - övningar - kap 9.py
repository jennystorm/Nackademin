kosmetika = 50
"""
# Övningsuppgift 9.1

infotext_1 = "Programmet räknar ut summan av\nalla heltal mellan 0-100000\nsamt summan av alla udda \nheltal mellan 0-500."
print ("*"*kosmetika)
print (infotext_1.center(kosmetika))
print ("*"*kosmetika)

jamna = 0
udda = 0

for i in range (0, 1000001):
    if i < 501:
        if i % 2 != 0:
            jamna += i
            udda += i
        else:
            jamna += i
    else:
        jamna += i

print (jamna)
print (udda, "\n")

# Övningsuppgift 9.2

infotext_2 = "Programmet går igenom 2 listor, en med registeringar och en med avanmälningar, och tar bort de som avanmält sig från anmälningslistan. ."
print ("*"*kosmetika)
print (infotext_2.center(kosmetika))
print ("*"*kosmetika)

registrerade =[" Anna ", "Eva ", " Erik ", " Lars ", " Karl "]
avanmalningar =[" Anna ", " Erik ", " Karl "]

for namn_1 in registrerade:
    for namn_2 in avanmalningar:
        if namn_1 == namn_2:
            registrerade.remove(namn_1)

print (registrerade, "\n")


# Övningsuppgift 9.3

infotext_3 = "Programmet kombinerar 2 listor."
print ("*"*kosmetika)
print (infotext_3.center(kosmetika))
print ("*"*kosmetika)

fornamn =[" Maria ", " Erik ", " Karl "]
efternamn =[" Svensson ", " Karlsson ", " Andersson "]

for namn_3 in fornamn:
    for namn_4 in efternamn:
        print (namn_3, namn_4)
print("\n")

# Övningsuppgift 9.4

infotext_4 = "Programmet kommer att skriva ut en lista i snygg punktform."
print ("*"*kosmetika)
print (infotext_4.center(kosmetika))
print ("*"*kosmetika)

todos = ["Städa", "Handla", "Plugga", "Ge blod"]

print(". : Att-göra: : .")
print("-"*18)

for i in todos:
    print("- " + i)

print ("\n")

"""

# Övningsuppgift 9.5

import os

infotext_5 = "Programmet är interaktivt med stack-funktion."
print ("*"*kosmetika)
print (infotext_5.center(kosmetika))
print ("*"*kosmetika)
print("\n")

stack = []

while True:
    # 1. Rensa terminalfönster
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    print(". : Stack-master : .")
    print("-" * kosmetika)
    if len(stack) == 0:
        print ("Stacken är tom.")
    else:
        for i in stack:
            print ("- " + i)
    print("-" * kosmetika)
    print(" | Meny | ")
    print("-" * kosmetika)
    print("push | Push element to stack")
    print("pull | Pull element from stack")
    print("exit | Exit program")
    print("-" * kosmetika)
    command = input("Meny > ")
    try:
        if command == "exit":
            break
        elif command == "pull":
            stack.pop()
        elif command == "push":
            command = input("Meny > ")
            stack.append(command)
        else:
            print("Felinmatat kommando.")
            command = input("Tryck enter för att börja om.")
    except:
        print("Stacken är tom.")
        command = input("Tryck enter för att börja om.")