person = {
    "firstname": "Johan",
    "lastname": "Svensson",
    "age": 25,
    "pets": [
        {"name": "Morris", "age": 3, "typ": "hund"},
        {"name": "Lisa", "age": 4, "typ": "katt"}
    ]
}

print("Jennys sätt (tar inte hänsyn till förändringar i listan):\n")
print(person["firstname"], person["lastname"], "är", person["age"], "år gammal och har 2 husdjur.")
print("* En", person["pets"][0]["age"], "är gammal", person["pets"][0]["typ"], "som heter", str(person["pets"][0]["name"]) +".")
print("* En", person["pets"][1]["age"], "är gammal", person["pets"][1]["typ"], "som heter", str(person["pets"][1]["name"]) +".")
print("\n")
print("Mahmuds sätt (tar hänsyn till förändringar i listan:\n")

namn = person["firstname"] + " " + person["lastname"]
ålder = person["age"]
count_pets = len(person["pets"])
pets = person["pets"]

print(F"{namn} är {ålder} år gammal och har {count_pets} husdjur." )

for pet in pets:
    print(F"* En {pet['age']} år gammal {pet['typ']} som heter {pet['name']}.")