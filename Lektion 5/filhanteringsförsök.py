f = open('textfil.txt', 'w')

f.write("Rad 1\n")
f.write("Nu har jag skrivit")

f = open('textfil.txt', 'r')

text = f.read()
print(text)

# Stänger endast filen, men det går även att ta bort filen  helt efter stängning
f.close()


attendants = ['Lisa', 'Kalle', 'Olivia', 'Johan']
with open('textfil.txt', 'w') as f:
    for attendant in attendants:
        f.write('Hello ' + attendant + '!\n')

