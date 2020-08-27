from RandomHelper import random_list

def bubbleSort(lista):
    print("Lista Original:")
    print(lista)
    #Função que implementa o método de ordenamento Bubble Sort.
    for i in range (0, len(lista)):
        for j in range (0, len(lista)-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print("\nLista Ordenada (Bubble Sort):")
    print(lista)


bubbleSort(random_list(20))