HoeveelMMS = int(input("Hoeveel M&M's moeten er aan de de worden toegevoegd? "))
import random

for i in range(HoeveelMMS):
    random = random.choice('OGBR')
print (random)
def MMZak(x):
    KleurenZak = ["oranje", "groen", "blauw", "bruin"]
    if x == "O":
        KleurenZak.append("oranje")
    elif x == "G":
        KleurenZak.append("groen")
    elif x == "B":
        KleurenZak.append("blauw")
    elif x == "R":
        KleurenZak.append("bruin")
    print (KleurenZak)


MMZak(random)
