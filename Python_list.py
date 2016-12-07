seznam = []

# seznam = ["A", "B", "C", "D", "E", "F"]

while True:
    print ("Zadej položku seznamu:")
    nova = input()
    if nova == "":
        break
    seznam.append(nova)


#print (seznam)

#print (str(seznam[0:-1]) + " and " + seznam[len(seznam)-1])


for i in seznam:
    if seznam.index(i) < len(seznam)-2:
        print (seznam[seznam.index(i)] + ", ", end = "")
    else :
        print (seznam[-2] + " a " + seznam[-1])
        break

exit = input()
