from RandomHelper import random_list
from random import randint

def linearSearch(lista, elemento):
    print("Lista:")
    print(lista)

    for i in lista:
        if i == elemento:
            return True
    return False

elemento = randint(1, 200)
print("A busca pelo elemento", elemento, "retornou", linearSearch(random_list(20), elemento))