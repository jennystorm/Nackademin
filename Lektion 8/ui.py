kosmetika = 40


def line (bool = False):
    if bool == True:
        print ("*"*kosmetika)
    else:
        print ( "-"*kosmetika)


def header (text):
    print("|",text.center(kosmetika))


def echo (text):
    print("|", text)


def prompt(text):
    command = input("| "+text+" > ")
    return command


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


def make_list(dict):
    teams_lista = []
    for i in dict:
        dict[i]["country"] = i
        teams_lista.append(dict[i])
    return teams_lista


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

