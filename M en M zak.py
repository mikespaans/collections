HoeveelMMS = int(input("Hoeveel M&M's moeten er aan de zak worden toegevoegd? "))
import random
KleurenZak = ["oranje", "groen", "blauw", "bruin"]


def MMZak(x: int):
    Zak = []
    for i in range(x):
        KleurKiezen = random.choice(KleurenZak)
        Zak.append(KleurKiezen)
        
    return Zak


print (MMZak(HoeveelMMS))