import random
AantalSpellen = random.randint(3,10)
spelList = ['Monoploly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']
def spelProgramma(spelList):
    print (spelList[ :AantalSpellen])

spelProgramma(spelList)
print (AantalSpellen)