"""Juvenal nao confia em ninguem."""


def explore(l, c, ultimo, cont):


    if 0 <= l < m and 0 <= c < n:
        if campo[l][c] == '.':
            cont = 0
            return True
        elif campo[l][c] == 't':
            if not ultimo == (l-1, c) or cont == 0:
                # explora pra cima
                cont += 1
                ultimo = (l+1, c)
                t1 = explore(l+1, c, ultimo, cont)
            else:
                t1 = True
            if not ultimo == (l+1, c) or cont == 0:
                # explora pra baixo
                cont += 1
                ultimo = (l-1, c)
                t4 = explore(l-1, c, ultimo, cont)
            else:
                t4 = True
            if not ultimo == (l, c-1) or cont == 0:
                # explora pra esquerda.
                cont += 1
                ultimo = (l, c+1)
                t2 = explore(l, c+1, ultimo, cont)
            else:
                t2 = True
            if not ultimo == (l, c+1) or cont == 0:
                # explora pra direita.
                cont += 1
                ultimo = (l, c-1)
                t3 = explore(l, c-1, ultimo, cont)
            else:
                t3 = True

            if t1 and t2 and t3 and t4:
                return True
        else:
            return False
    else:
        cont = 0
        return True


def tiro(l, c):
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
    l, c = input().split()
    l, c = int(l) - 1, int(c) - 1

    if campo[l][c] == '#':
        tiro(l, c)
        ultimo = (l, c)
        if explore(l, c, ultimo, 0) == True:
            naviosAfundados += 1

print(naviosAfundados)