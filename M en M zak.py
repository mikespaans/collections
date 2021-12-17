HoeveelMMS = int(input("Hoeveel M&M's moeten er aan de zak worden toegevoegd? "))
import random


def MMZak(x: int):
    KleurenZak = ["oranje", "groen", "blauw", "bruin"]
    for i in range(x):
        KleurKiezen = random.choice('OGBR')
        if KleurKiezen == "O":
            KleurenZak.append("oranje")
        elif KleurKiezen == "G":
            KleurenZak.append("groen")
        elif KleurKiezen == "B":
            KleurenZak.append("blauw")
        elif KleurKiezen == "R":
            KleurenZak.append("bruin")
    print (KleurenZak)


MMZak(HoeveelMMS)