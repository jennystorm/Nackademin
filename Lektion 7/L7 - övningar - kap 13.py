import requests
import json
kosmetika = 30

# Övningsuppgift 13.1


number = input("Mata in ett positivt heltal >")
response = requests.get("https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=" + number)
response_dict = json.loads(response.text)

if response_dict["even"] == True:
    print(number + " är ett jämnt heltal.")
else:
    print(number, "är ett ojämnt heltal.")
if response_dict["prime"] == True:
    print("Det är även ett primtal.")
else:
    print("Det är inte ett primta.")
print("Numrets faktorer är: ")
for i in response_dict["factors"]:
    print (i)

# Övningsuppgift 13.2

while True:
    city = input("Enter the name of the city for which you want forecasts: \n> ")
    city = city.lower()
    city_copy = city.replace("å", "a")
    city_copy = city_copy.replace("ä", "a")
    city_copy = city_copy.replace("ö", "o")
    try:
        forecast = requests.get("https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/" + city_copy)
        forecast = json.loads(forecast.text)
        city = city.capitalize()
        print("-"*kosmetika)
        print(("FORCAST").center(kosmetika))
        print(city.center(kosmetika))
        print("-" * kosmetika)
        for i in forecast["forecasts"]:
            print(i["date"], "\t", (i["forecast"]).capitalize())
    except:
        print("City not found.")
    command = input("Press enter to continue or 0 to exit.")
    if command == "0":
        break
    else:
        continue


#Övningsuppgift 13.3

while True:
    artists = requests.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/")
    artists_dict = json.loads(artists.text)
    print("-"*kosmetika)
    print(("--- Artist DB ---").center(kosmetika))
    print("-"*kosmetika)
    for i in artists_dict["artists"]:
        print(i["name"])
    print("-"*kosmetika)
    command = input("Select artist:\n> ")
    command = command.title()
    try:
        for i in artists_dict["artists"]:
            if i["name"] == command:
                id = i["id"]
        artist = requests.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + id)
        artist_dict = json.loads(artist.text)
        print("-" * kosmetika)
        print(command.center(kosmetika))
        print("*"*kosmetika)
        print("Genres:")
        print(*artist_dict["artist"]["genres"], sep=", ")
        print("Years active:")
        print(*artist_dict["artist"]["years_active"], sep=", ")
        print("Members:")
        print(*artist_dict["artist"]["members"], sep=", ")
        print("*" * kosmetika)
        id = 0
    except:
        print("Artist not found.")
    command = input("Press enter to continue or 0 to exit.")
    if command == "0":
        break
    else:
        continue

# Använd istället ", ".join(listan[listan]) för snyggare utskrift
