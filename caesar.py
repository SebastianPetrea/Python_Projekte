

def caezar_verschluesselung(eingabe):
    wort = ""
    verschiebung = 0

    for i in eingabe: 
        verschiebung += 1
        asci = ord(i)
        if asci in range(65,91):
            if (asci + verschiebung) > 90:
                asci = ((asci + verschiebung) % 91) + 65
            else:
                asci += verschiebung 
            ausgabe = chr(asci)
            wort += ausgabe
        elif asci in range(97,123):
            if (asci + verschiebung) > 122:
                asci = ((asci + verschiebung) % 122) + 96 
            else:
                asci += verschiebung
            ausgabe = chr(asci)
            wort += ausgabe
        else:
            return "Falsche Eingabe"

    return wort 
    


eingabe = input("Geben Sie ein Wort ein, der Verschlusselt werden soll : ")
print(caezar_verschluesselung(eingabe))


