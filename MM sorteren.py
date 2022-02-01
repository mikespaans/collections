HoeveelMMS = int(input("Hoeveel M&M's moeten er aan de zak worden toegevoegd? "))
import random

def ZakSorteren(x):
    GesoorterdeZak = sorted(x) 
    print (type(GesoorterdeZak))
    return GesoorterdeZak

KleurenZak = ["oranje", "groen", "blauw", "bruin"]

def MMZak(x: int):
    Zak = []
    for i in range(x):
        KleurKiezen = random.choice(KleurenZak)
        Zak.append(KleurKiezen)
        
    return Zak

print (ZakSorteren(MMZak(HoeveelMMS)))

def MMSZak(x: int):
    Zak = {
    "oranje" : 0,
    "groen" : 0,
    "blauw" : 0,
    "bruin" : 0
    }
    for i in range (x):
        KleurKiezen = random.choice(KleurenZak)
        Zak[KleurKiezen] += 1
    return Zak
      
print(ZakSorteren(MMSZak(HoeveelMMS)))