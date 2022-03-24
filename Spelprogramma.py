import random
AantalSpellen = random.randint(3,10)
spelList = ['Monoploly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma(x):
    NieuweSpelList = []
    for i in range(x):
        RandomSpel = random.choice(spelList)
        NieuweSpelList.append(RandomSpel)
    return NieuweSpelList

print (spelProgramma(AantalSpellen))