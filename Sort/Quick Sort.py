import random

def quickSort(lista):
    #Função que implementa o método de ordenamento Quick Sort.
    L=[]
    R=[]
    if len(lista) <= 1:
        return lista
    chave = lista [len(lista)//2]
    for i in lista:
        if i < chave:
            L.append(i)
        if i > chave:
            R.append(i)
    return quickSort(L)+[chave]+quickSort(R)

def listaRan(tam, lista):
    #Função gera uma 'lista' com 'tam' valores aleatórios.
    random.seed()
    i=0
    while i<tam:
        num = random.randint(1, 10*tam)
        if num not in lista:
            lista.append(num)
            i+=1
    print("Lista Original:")
    print(lista)

lista = []
listaRan(20, lista)
lista = quickSort(lista)
print("\nLista Ordenada (Quick Sort):")
print(lista)