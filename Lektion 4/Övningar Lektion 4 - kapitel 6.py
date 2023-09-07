# Övningsuppgift 6.3

palindrom = input("Skriv in ordet eller meningen du tror är ett palindrom: ")
testversion = palindrom
testversion = testversion.lower()
testversion = testversion.replace(" ", "")
fram = 0
bak = -1

while fram < len(testversion):
    if testversion[fram] == testversion[bak]:
        print(testversion[fram], "=", testversion[bak])
        fram += 1
        bak += -1
    else:
        print ("detta gick inte bra")
        break

if fram == len(testversion):
    print ("\"", palindrom, "\"", "är ett palindrom.")
else:
    print("\"", palindrom, "\"", "är inte ett palindrom.")
