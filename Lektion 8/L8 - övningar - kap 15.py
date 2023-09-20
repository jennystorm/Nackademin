"""

# Övningsuppgift 15.1
# Sortera en lista och skriv ut med rutor

persons = ["Alice", "Lucas", "Olivia", "Liam", "Astrid", "William"]

persons.sort()
for person in persons:
    print ("[ ]", person)

# Övningsuppgift 15.2
# Sortera en lista med nummer, skriv ut innan och efter sortering

import random
numbers = []
for x in range (10):
    numbers.append (random.randint(0 ,20))

print("Unsorted:")
for number in numbers:
    print ("-", number)

numbers.sort()

print("Sorted:")
for number in numbers:
    print ("-", number)

"""

# Övningsuppgift 14.3

import ui


teams = {
    "Brazil" : {
        "wins" : 0 ,
        "draws" : 0 ,
        "losses" : 0 ,
        "goals for" : 0 ,
        "goals against" : 0
    } ,
    "Serbia": {
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals for": 0,
        "goals against": 0
    },
    "Switzerland" : {
        "wins" : 0 ,
        "draws" : 0 ,
        "losses" : 0 ,
        "goals for" : 0 ,
        "goals against" : 0
    } ,
    "Costa Rica" : {
        "wins" : 0 ,
        "draws" : 0 ,
        "losses" : 0 ,
        "goals for" : 0 ,
        "goals against" : 0
    } ,
}

# 17 June 2018 #
ui.add_game (teams,"Costa Rica", 0 , "Serbia", 1)
ui.add_game (teams,"Brazil", 1 , "Switzerland", 1)
# 22 June 2018 #
ui.add_game (teams,"Brazil", 2 , "Costa Rica", 0)
ui.add_game (teams,"Serbia", 1 , "Switzerland", 2)
# 27 June 2018 #
ui.add_game (teams,"Serbia", 0 , "Brazil", 2)
ui.add_game (teams,"Switzerland", 2 , "Costa Rica", 2)

teams_list = []
teams_list = ui.make_list(teams)

#def sort_list(list):

for i in teams_list:
    points = (i["wins"] * 3) + i["draws"]
    print(i["country"], points)
