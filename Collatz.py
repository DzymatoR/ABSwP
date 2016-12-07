

# zadej cislo

while True:
    try:
        cislo = int(input("zadej cislo: "))
        break
    except ValueError:
        print("Nezadal jsi celé číslo")


print("Zadals: " + str(cislo))


# funkce collatzova sekvence

def collatz(a):
    if a % 2 == 0:
        b = a // 2
    else:
        b = a * 3 + 1
    return b

# provedení

while int(cislo) >= 1:
    cislo = collatz(int(cislo))
    print(str(cislo))
    if int(cislo) == 1:
        break
