import random

#Listen
Adjektive = ["beste", "liebenswürdigste", "schönste", "größte"]
Nomen = ["Mensch", "Hecht", "Freund", "Kumpel"]
print("Du bist der",end= " ")

#Zufall
print(random.choice(Adjektive), end =" ")
print(random.choice(Nomen))

