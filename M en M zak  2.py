HoeveelMMS = int(input("Hoeveel M&M's moeten er aan de de worden toegevoegd? "))
import random

def MMZak(x: int):
    KleurenZak = {
        "oranje" : 0,
        "groen" : 0,
        "blauw" : 0,
        "bruin" : 0
    }
    for i in range (x):
        KleurKiezen = random.choice('OGBR')
        print (KleurKiezen)
        if KleurKiezen == "O":
            KleurenZak["oranje"] += 1
        elif KleurKiezen == "G":
            KleurenZak["groen"] += 1
        elif KleurKiezen == "B":
            KleurenZak["blauw"] += 1
        elif KleurKiezen == "R":
            KleurenZak["bruin"] += 1
    print (KleurenZak)
MMZak(HoeveelMMS)