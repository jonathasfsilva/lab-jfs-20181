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

def explorarCima(l, c, campo):
    """Explora Cima."""
    if 0 <= c-1 and campo[l-1][c] == '.' or c-1 < 0:
        return True
    elif campo[l-1][c] == 't':
        explorarCima(l-1, c, campo)
    else:
        return False


def explorarBaixo(l, c, campo, m):
    """Explora em baixo."""
    if l+1 <= m and campo[l+1][c] == '.' or l+1 > m:
        return True
    elif campo[l+1][c] == 't':
        explorarBaixo(l+1, c, campo, m)
    else:
        return False


def explorarEsquerda(l, c, campo):
    """Explora na esquerda."""
    if 0 <= c-1 and campo[l][c-1] == '.' or c-1 < 0:
        return True
    elif campo[l][c-1] == 't':
        explorarEsquerda(l, c, campo)
    else:
        return False


def explorarDireita(l, c, campo, n):
    """Explora na direita."""
    if c+1 <= n and campo[l][c+1] == '.' or n < c+1:
        return True
    elif campo[l][c+1] == 't':
        explorarDireita(l, c, campo, n)
    else:
        return False


def explorar(l, c, campo, m, n):
    """Funçao master."""
    cima = explorarCima(l, c, campo)
    baixo = explorarBaixo(l, c, campo, m)
    esquerda = explorarEsquerda(l, c, campo)
    direita = explorarDireita(l, c, campo, n)

    if cima == baixo == esquerda == direita:
        return True