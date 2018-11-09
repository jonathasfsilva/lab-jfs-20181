u"""Algoritmos de Ordenação.

- BublleSort
- InsertSort
- MergeSort
- QuickSort
- SelectSort

"""
# dfdf

def mergeSort(lista):
    """MergeSort.

    Recebe uma lista e retorna a lista ordenada por mergeSort.
    """
    if len(lista) > 1:
        meio = len(lista)//2
        ladoDireito = lista[:meio]
        ladoEsquerdo = lista[meio:]
        mergeSort(ladoDireito)
        mergeSort(ladoEsquerdo)
        i, j, k = 0, 0, 0
        while i < len(ladoEsquerdo) and j < len(ladoDireito):
            if ladoEsquerdo[i] < ladoDireito[j]:
                lista[k] = ladoEsquerdo[i]
                i += 1
            else:
                lista[k] = ladoDireito[j]
                j += 1
            k += 1
        while i < len(ladoEsquerdo):
            lista[k] = ladoEsquerdo[i]
            i += 1
            k += 1
        while j < len(ladoDireito):
            lista[k] = ladoDireito[j]
            j += 1
            k += 1
        return lista


def bublleSort(lista):
    """BublleSort.

    Recebe uma lista e retorna ela ordenada por bublleSort.
    """
    listaConfere = []
    for j in range(len(lista)):
        listaConfere = lista[::]
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
        if listaConfere == lista:
            break
    return lista


def insertSort(lista):
    """InsertSort.

    Recebe uma lista e retona ela ordenada por insertSort.
    """
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i
        while j > 0 and lista[j-1] > chave:
            lista[j] = lista[j-1]
            j -= 1
        lista[j] = chave
    return lista


def selectSort(lista):
    """SelectSort.

    Recebe uma lista e retona ela ordenada por SelectSort.
    """
    n = len(lista)
    for i in range(len(lista)-1):
        mini = i
        for j in range(i+1, n):
            if lista[j] < lista[mini]:
                mini = j
        lista[i], lista[mini] = lista[mini], lista[i]
    return lista


def quickSort(lista):
    """QuickSort.

    Recebe uma lista e retorna ela orenada por QuickSort.
    """
    if len(lista) <= 1:
        return lista
    less, equal, greater = [], [], []
    pivot = lista[0]
    for x in lista:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return quickSort(less) + equal + quickSort(greater)

def quickSortRev(lista):
    """QuickSort.

    Recebe uma lista e retorna ela ordenada reversamente por QuickSort.
    """
    if len(lista) <= 1:
        return lista
    less, equal, greater = [], [], []
    pivot = lista[0]
    for x in lista:
        if x > pivot:
            greater.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            less.append(x)
    return quickSortRev(greater) + equal + quickSortRev(less)

l = [1,2,3,4,5,6]
print(quickSortRev(l))
