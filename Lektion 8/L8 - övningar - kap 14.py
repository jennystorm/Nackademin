"""
# Övningsuppgift 14.1
# Omvandla km/miles med hjälp av funktioner

def km_to_miles(distance):
    return distance * 0.6214


def miles_to_km(distance):
    return distance * 1.6214


question = input("Ange distans: ")
unit= ""
distance = ""

for i in question:
    if i.isdigit() == False:
        unit += i
    else:
        distance += i

unit = unit.lstrip()
distance = int(distance)

if unit[0] == "m":
    print(distance, unit, "is", miles_to_km(distance), "km.")

elif unit[0] == "k":
    print(distance, unit, "is", km_to_miles(distance), "miles.")
else:
    print("Unit", unit, "not identified.")

# Övningsuppgift 14.2
# Skapa modul med samling funktioner som förenklar vid utveckling av gränssnitt för terminaler

import ui

ui.line()
ui.header("EXEMPEL")
ui.line(True)
ui.echo("Detta är ett exempel på hur")
ui.echo("ett gränssnitt kan se ut")
ui.line()
ui.header("Vad vill du göra?")
ui.line()
ui.echo("A | Visa")
ui.echo("B | Ändra")
ui.line()
command = ui.prompt("Val")



# Övningsuppgift 14.3
# Skapa en funktion för att plocka ut jämna tal i en lista

import random
numbers = []
for x in range (10):
    numbers.append ( random.randint (0 ,9))

print(numbers)

def get_even(list):
    even = []
    for i in list:
        if i %2 == 0:
            even.append(i)
    return even

even = get_even (numbers)
print ("even :", even )
print ("numbers :", numbers )

"""

# Övningsuppgift 14.4

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


def add_game(teams, home_team, home_score, away_team, away_score):
    teams[home_team]["goals for"] += home_score
    teams[home_team]["goals against"] += away_score
    teams[away_team]["goals for"] += away_score
    teams[away_team]["goals against"] += home_score
    if home_score == away_score:
        teams[home_team]["draws"] += 1
        teams[away_team]["draws"] += 1
    elif home_score > away_score:
        teams[home_team]["wins"] += 1
        teams[away_team]["losses"] += 1
    else:
        teams[home_team]["losses"] += 1
        teams[away_team]["wins"] += 1

# 17 June 2018 #
add_game (teams, "Costa Rica", 0 , "Serbia", 1)
add_game (teams, "Brazil", 1 , "Switzerland", 1)
# 22 June 2018 #
add_game (teams, "Brazil", 2 , "Costa Rica", 0)
add_game (teams, "Serbia", 1 , "Switzerland", 2)
# 27 June 2018 #
add_game (teams, "Serbia", 0 , "Brazil", 2)
add_game (teams, "Switzerland", 2 , "Costa Rica", 2)

print("----------------------------------------")
print("| Nation\t\t| W | D | L | GF | GA |")
print("----------------------------------------")
print("| Brazil\t\t|", teams["Brazil"]["wins"], "|", teams["Brazil"]["draws"], "|", teams["Brazil"]["losses"], "|", teams["Brazil"]["goals for"], " |", teams["Brazil"]["goals against"], " |")
print("| Serbia\t\t|", teams["Serbia"]["wins"], "|", teams["Serbia"]["draws"], "|", teams["Serbia"]["losses"], "|", teams["Serbia"]["goals for"], " |", teams["Serbia"]["goals against"], " |")
print("| Switzerland\t|", teams["Switzerland"]["wins"], "|", teams["Switzerland"]["draws"], "|", teams["Switzerland"]["losses"], "|", teams["Switzerland"]["goals for"], " |", teams["Switzerland"]["goals against"], " |")
print("| Costa Rica\t|", teams["Costa Rica"]["wins"], "|", teams["Costa Rica"]["draws"], "|", teams["Costa Rica"]["losses"], "|", teams["Costa Rica"]["goals for"], " |", teams["Costa Rica"]["goals against"], " |")
print("----------------------------------------")




# Övningsuppgift 14.5
# Gör om dictionary till en lista med dictionary i med hjälp av en function
# Förbättring: borde gå att göra en tabell mindre beroende av vad som står i den
# Mahmuds förslag är att först skapa en ny dictionary, och därefter append:a den till lista
# country_dict = { "country" : i, "wins" : dict[i]["wins"] }

teams_lista = []

def make_list(dict):
    for i in dict:
        dict[i]["country"] = i
        teams_lista.append(dict[i])
    return teams_lista

teams_lista = make_list(teams)





#Övningsuppgift 14.6
# Gör en funktion som skriver ut listan med dictionary i en tabell

def print_table(list):
    counter = 1
    print("""−−−−−−−−−−−−−−−−−−−−−−-−−−−−−−−−−−−−−−−−−−−−−−−−−−−
| # | Nation       | W | D | L | GF | GA | GD | P |
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−-−−−−−−−−−−−−−−−−−−−−""")
    for i in list:
        space = 11 - len(i["country"])
        difference = i["goals for"] - i["goals against"]
        space_2 = 2 - len(str(difference))
        points = (i["wins"]*3)+i["draws"]
        print ("|", counter, "|", i["country"], space*" ", "|", i["wins"], "|", i["draws"], "|", i["losses"], "|", i["goals for"], " |", i["goals against"], " |"+space_2*" ",difference, "|", points, "|")
        counter += 1
    print("−−−−−−−−−−−−−−−−−−−−−−-−−−−−−−−−−−−−−−−−−−−−−−−−−−−")

print_table(teams_lista)

