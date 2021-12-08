import random
AantalSpellen = random.randint(3,10)
spelList = ['Monoploly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']
def spelProgramma(spelList, minimum):
    print (spelList[minimum :])

spelProgramma(spelList, AantalSpellen)
