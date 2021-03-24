import random

a = [1,2,3]
b = 0
punkte = 0

while b <= 2:
    eingabe = int(input("Wählen Sie zwischen: Stein[1], Papier[2] oder Schere[3]"))
    liste = random.choice(a)
    if eingabe == liste:
        print("Du =", eingabe, "\nComputer =", liste, "\n>>Gleichstand")
    elif eingabe == 1 and liste == 2:
        print("Du =", eingabe, "\nComputer =", liste ,"\n>>Papier schlägt Stein.\nDu wurdest besiegt")
        punkte = punkte -1
    elif eingabe == 1 and liste == 3:
        print("Du =",eingabe,"\nComputer =", liste, "\n>>Stein schlägt Schere.Gewonnen!")
        punkte = punkte +1
    elif eingabe == 2 and liste == 1:
        print("Du =",eingabe,"\nComputer =", liste, "\n>>Papier schlägt Stein.","Gewonnen!")
        punkte = punkte +1
    elif eingabe == 2 and liste == 3:
        print("Du =", eingabe, "\nComputer =", liste, "\n>>Schere schlägt Papier.Du wurdest besiegt!")
        punkte = punkte -1
    elif eingabe == 3 and liste == 1:
        print("Du =", eingabe, "\nComputer =", liste, "\n>>Stein Schlägt Schere. Du wurdest besiegt!")
        punkte = punkte -1
    elif eingabe == 3 and liste == 2:
        print("Du =", eingabe, "\nComputer =", liste, "\n>>Schere schlägt Papier. Gewonnen!")
        punkte = punkte +1
    b += 1
   

print("Du hast:",punkte, "punkte ereicht")
