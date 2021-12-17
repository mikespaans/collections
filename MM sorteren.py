HoeveelMMS = int(input("Hoeveel M&M's moeten er aan de zak worden toegevoegd? "))
import random
def MMSorteren(y):
    return e['number']
def ZakSorteren(x):
    x.sort() 
    return x
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
    ZakSorteren(KleurenZak)
    print (KleurenZak)
    

MMZak(HoeveelMMS)

def MMSZak(x: int):
    KleurZak = {
        "oranje" : 0,
        "groen" : 0,
        "blauw" : 0,
        "bruin" : 0
    }
    for i in range (x):
        KleurKiezen = random.choice('OGBR')
        if KleurKiezen == "O":
            KleurZak["oranje"] += 1
        elif KleurKiezen == "G":
            KleurZak["groen"] += 1
        elif KleurKiezen == "B":
            KleurZak["blauw"] += 1
        elif KleurKiezen == "R":
            KleurZak["bruin"] += 1
    print (KleurZak)
    KleurZak.sort(key=MMSorteren)
    print (KleurZak)
MMSZak(HoeveelMMS)