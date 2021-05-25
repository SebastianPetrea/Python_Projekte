"""******************************************
********Variationen ohne Wiederhollungen*****
*********************************************
"""

#Benutzer eingbae
eingabe_n = int(input("n: "))
eingabe_k = int(input("k: "))

#Variablen erstellen
fakultät = 1
fakultät_1 = 1
k = eingabe_n - eingabe_k
#n! berechnen
while eingabe_n > 0:
        fakultät = fakultät * eingabe_n
        eingabe_n = eingabe_n -1
#k! berechnen
if k == 0:
        k = 1
while k > 0:    
        fakultät_1 = fakultät_1 * k
        k = k - 1

ergebnis = (fakultät / fakultät_1) 

print(ergebnis)


