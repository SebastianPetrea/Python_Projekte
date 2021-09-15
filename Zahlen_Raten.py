
import random 

#Zufällige Zahl zwischen 1-20 
zahlen_random = random.randrange(1,20)

aktiv = True
versuche = 6

#Versuche
while aktiv:
    versuche = versuche - 1
    print("Die Zahl liegt zwischen 1-20")
    print("-Du hast noch: ",versuche, "versuche.")
    #Benutzer eingabe
    eingabe = int(input("Wie lautet die Zahl?"))

    if zahlen_random == eingabe:
        print("Huuraa du hast es erraten!")
        aktiv = False
        break
    #Hinweis
    elif eingabe < zahlen_random:
        print("!! Die Zahl ist größer. !!")
    elif eingabe > zahlen_random : 
        print("!! Die Zahl ist kleiner. !!")
    
    #Versuche
    if (versuche == 0):
        print("Leider Verloren :( \nVerusch es noch einmal :)")
        print("Die zahl wahr: ", zahlen_random)
        aktiv = False









