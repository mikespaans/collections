ListOne = [1,2,3,4,5,6,7,8,9,10]
ListTwo = [2,4,6,8,10,12,14,16,18,20]


    

def plus(list1, list2):
    for i in range(len(list1)):
        print(list1[i] + list2[i])
plus(ListOne, ListTwo)

def min(list1, list2):
    for i in range(len(list1)):
        print(list1[i] - list2[i])
min(ListOne, ListTwo)

def keer(list1, list2):
    for i in range(len(list1)):
        print(list1[i] * list2[i])
keer(ListOne, ListTwo)

def gedeeld(list1, list2):
    for i in range(len(list1)):
        print(list1[i] / list2[i])
gedeeld(ListOne, ListTwo)

