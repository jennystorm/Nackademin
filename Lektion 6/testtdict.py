test = { "hej":"på dig", "jag":"heter Jenny", "nu":"har jag nog exempel"}
while True:
    command = input("hitta")
    for i in test:
        if i == command:
            print("This will delete", i, test[command])
            command_2 = input("Vill du fortsätta? Y/N >")
            if command_2 == "Y":
                del test[command]
                break
            elif command_2 == "N":
                print("Det tas ej bort")
            else:
                print("något gick fel")