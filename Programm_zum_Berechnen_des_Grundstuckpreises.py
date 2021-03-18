"""**************************************************
***-Programm zum Berechnen des Grundstucks Preis-"***
**************************************************"""

#Einlesen der Werte
lange = int(input("Geben Sie die Länge in Meter ein:"))
breite = int(input("Geben Sie die Breite in Meter ein:"))
preis_pro_Quadratmeter = float(input("Geben Sie den Preis pro Quadratmeter ein:"))

#addieren und ausgeben
ergebnis = (lange * breite) * preis_pro_Quadratmeter
print("Der Preis beträgt:", ergebnis, "Euro")

