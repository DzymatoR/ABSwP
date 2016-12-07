birthday = {"Jouza": "Leden 3", "Katka": "Listopad 14", "Teri": "Srpen 26", "Kuba": "Září 11"}

while True:
    print("Zadej jméno: ", end="")
    jmeno = input()
    if jmeno == "":
        break

    if jmeno in birthday:
        print(jmeno + " má narozeniny " + birthday[jmeno])
    else:
        print("Nemám informace o: " + jmeno)
        print("Jaké je datum narození této osoby?: ")
        bday = input()
        birthday[jmeno] = bday
        print("Databáze byla aktualizována")
        print(birthday)
