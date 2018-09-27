u"""Tools.

Tools for Lab de Programação.
"""


def sucessor(x):
    """Returna o sucessor."""
    x += 1
    return x


def soma(x, y):
    """Soma com sucessores."""
    s = x
    for i in range(y):
        s = sucessor(s)
    return s


def multiplica(x, y):
    """Multiplica com soma."""
    s = 0
    for i in range(y):
        s = soma(s, x)
    return s


def exponicia(x, y):
    """Exponiaciacao com multicicacao."""
    s = 1
    for i in range(y):
        s = multiplica(s, x)
    return s


def insertionSort(lista):
    """Insertionsort. Recebe lista, retorna ordenado, ordem crescente."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j
        while i > 0 and lista[i-1] > chave:
            lista[i] = lista[i-1]
            i = i-1
        lista[i] = chave
    return lista


def insertionSortRev(lista):
    """Insertionsort. Recebe lista, retorna ordenado, ordem decrescente."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j
        while i > 0 and lista[i-1] < chave:
            lista[i] = lista[i-1]
            i = i-1
        lista[i] = chave
    return lista
