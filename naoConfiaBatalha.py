"""Juvenal nao confia em ninguem."""


def exploraDiagPriAsc(l, c, campo, m, n):
    """Explora diagonal primaria ascendente."""
    if l+1 <= m-1 and c+1 <= n-1:
        if campo[l+1][c+1] == '.':
            pass
        elif campo[l+1][c+1] == 't':
            exploraDiagPriAsc(l+1, c+1, campo, m, n)
        elif campo[l+1][c+1] == '#':
            return False
    elif m < l+1 or n < c+1:
        pass
    else:
        return False


def exploraDiagPriDes(l, c, campo, m, n):
    """Explora diagonal primaria descendente."""
    if m-1 <= l-1 and n-1 <= c-1:
        if campo[l-1][c-1] == '.':
            pass
        elif campo[l-1][c-1] == 't':
            exploraDiagPriDes(l-1, c-1, campo, m, n)
        elif campo[l-1][c-1] == '#':
            return False
    elif l-1 < m or c-1 < n:
        pass
    else:
        return False


def explorarCima(l, c, campo):
    """Explora Cima."""
    if 0 <= l-1:
        if campo[l-1][c] == '.':
            pass
        elif campo[l-1][c] == 't':
            explorarCima(l-1, c, campo)
        elif campo[l-1][c] == '#':
            return False
    elif l-1 < 0:
        pass
    else:
        return False


def explorarBaixo(l, c, m):
    """Explora em baixo."""
    if l+1 <= m-1:
        if campo[l+1][c] == '.':
            pass
        elif campo[l+1][c] == 't':
            explorarBaixo(l, c, campo, m)
        elif campo[l+1][c] == '#':
            return False
    elif m-1 < l+1:
        pass
    else:
        return False


def explorarEsquerda(l, c, campo):
    """Explora na esquerda."""
    if 0 <= c-1:
        if campo[l][c-1] == '.':
            pass
        elif campo[l][c-1] == 't':
            explorarEsquerda(l, c-1, campo)
        elif campo[l][c-1] == '#':
            return False
    elif c-1 < 0:
        pass
    else:
        return False


def explorarDireita(l, c, campo, n):
    """Explora na direita."""
    if c+1 <= n-1:
        if campo[l][c+1] == '.':
            pass
        elif campo[l][c+1] == 't':
            explorarDireita(l, c+1, campo, n)
        elif campo[l][c+1] == '#':
            return False
    elif n-1 < c+1:
        pass
    else:
        return False


def explorar(l, c, campo, m, n):
    """Funçao master."""
    cima = explorarCima(l, c, campo)
    baixo = explorarBaixo(l, c, campo, m)
    esquerda = explorarEsquerda(l, c, campo)
    direita = explorarDireita(l, c, campo, n)
    diagPriAsc = exploraDiagPriAsc(l, c, campo, m, n)
    diagPriDes = exploraDiagPriDes(l, c, campo, m, n)

    if cima == baixo == esquerda == direita == diagPriAsc == diagPriDes:
        return True

def explorar2(l, c, campo, m, n):
    explorar2(l-1, c, campo, m, n)



def tiro(l, c, campo):
    """Da o tiro."""
    if campo[l][c] == '#':
        campo[l][c] = 't'


m, n = input().split()
m, n = int(m), int(n)

campo = []

naviosAfundados = 0

for i in range(m):
    linha = []
    entrada = input()
    for j in range(n):
        linha.append(entrada[j])
    campo.append(linha)

jogadas = int(input())

for i in range(jogadas):
    jogada = input().split()
    l, c = jogada
    l, c = int(l)-1, int(c)-1

    if campo[l][c] == '#':
        tiro(l, c, campo)
        if explorar(l, c, campo, m, n):
            naviosAfundados += 1

print(naviosAfundados)