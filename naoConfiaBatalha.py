"""Juvenal nao confia em ninguem."""


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


def explorarBaixo(l, c, campo, m):
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

    if cima == baixo == esquerda == direita:
        return True


def tiro(l, c, campo):
    """Da o tiro."""
    if campo[l][c] == '#':
        campo[l][c] = 't'


tamanho = input().split()

m, n = tamanho
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