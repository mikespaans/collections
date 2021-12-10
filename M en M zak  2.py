HoeveelMMS = int(input("Hoeveel M&M's moeten er aan de de worden toegevoegd? "))
import random

for i in range(HoeveelMMS):
    KleurKiezen = random.choice('OGBR')
    print (KleurKiezen)
def MMZak(x):
    KleurenZak = ["oranje", "groen", "blauw", "bruin"]
    for i in range(HoeveelMMS):
        if x == "O":
            KleurenZak.append("oranje")
        elif x == "G":
            KleurenZak.append("groen")
        elif x == "B":
            KleurenZak.append("blauw")
        elif x == "R":
            KleurenZak.append("bruin")
        print (KleurenZak)


MMZak(KleurKiezen)
