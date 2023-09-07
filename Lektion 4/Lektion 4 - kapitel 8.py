kosmetika = 20
# Övningsuppgift 8.1
# Skriv ut städa, plugga, handla som sträng
print ("-"*kosmetika)
print ("Skriv ut som sträng.")
print ("-"*kosmetika)
todos = ["Städa", "Handla", "Plugga", "Ge blod"]
print(todos[0])
print(todos[2])
print(todos[1])
print ("\n\n")


# Övningsuppgift 8.24
# Genom interaktion med användare ska ditt script lägga till en sträng till listan.
print ("-"*kosmetika)
print ("Lägg till punktt.")
print ("-"*kosmetika)
todos = ["Städa", "Handla", "Plugga", "Ge blod"]
print (todos)
ny = input("Lägg till en punkt på att-göra-listan:")
todos.append(ny)
print (todos)
print ("\n\n")


# Övningsuppgift 8.3.
# Ditt script ska nu låta användare ta bort en punkt genom att mata in dess index.
print ("-"*kosmetika)
print ("Ta bort punkt.")
print ("-"*kosmetika)
todos = ["Städa", "Handla", "Plugga", "Ge blod"]
print (todos)
ny = int(input("Vilken punkt på att-göra-listan vill du ta bort?"))
del todos[ny]
print (todos)
print ("\n\n")


# Övningsuppgift 8.4.
# Ditt script ska nu låta användare ta bort en punkt genom att mata in dess värde.
print ("-"*kosmetika)
print ("Ta bort punkt.")
print ("-"*kosmetika)
todos = ["Städa", "Handla", "Plugga", "Ge blod"]
print (todos)
ny = input("Ta bort en punkt på att-göra-listan:")
todos.remove(ny)
print (todos)
print ("\n\n")



# Övningsuppgift 8.5
# Mata in en ny punkt och sedan sortera i bokstavsordning
print ("-"*kosmetika)
print ("Lägga till och sortera i bokstavsordning.")
print ("-"*kosmetika)
todos = ["Städa", "Handla", "Plugga", "Ge blod"]
print (todos)
ny = input("Lägg till en punkt på att-göra-listan:")
todos.append(ny)
todos.sort()
print (todos)
print ("\n\n")


# Övningsuppgift 8.6
# Söka i listan efter särskilt element och fråga användaren om elementet ska läggas till
print ("-"*kosmetika)
print ("Sök i listan.")
print ("-"*kosmetika)
todos = ["Städa", "Handla", "Plugga", "Ge blod"]
print (todos)
ny = input("Vilken punkt vill du leta efter?")
if ny in todos:
    print ("Punkten finns i listan.")
    print (todos)
else:
    print ("Punkten finns inte i listan.")
    fraga = input("Vill du lägga till punkten till att-göra-listan? J/N")
    if fraga == "J":
        todos.append(ny)
        print (todos)
    else:
        print ("Du la inte till punkten i listan.")
        print (todos)

