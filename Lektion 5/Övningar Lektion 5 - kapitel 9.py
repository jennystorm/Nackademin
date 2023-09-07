kosmetika = 50


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

fornamn =[" Maria ", " Erik ", " Karl "]
efternamn =[" Svensson ", " Karlsson ", " Andersson "]

for namn_3 in fornamn:
    for namn_4 in efternamn:
        print (namn_3, namn_4)


# Övningsuppgift 9.4
