"""Colheita de Caju."""

def montaMatriz(l, c):
    """Monta a matriz."""
    matriz = []
    for i in range(l):
        entrada = input().split()
        line = []
        for j in range(c):
            line.append(int(entrada[j]))
        matriz.append(line)
    return matriz


def somaMatrizSec(x, y, l, c, m, n, matriz):
    """Faz a soma da matriz secundaria."""
    fatias = []

    for i in range(x, l - m):
        for j in range(y, c - n):
            fatia = matriz[i][j:n]
            if len(fatia) == n:
                fatias.append(sum(fatia))

    return sum(fatias)


tamanhos = input().split()
l, c, m, n = tamanhos
l, c, m, n = int(l), int(c), int(m), int(n)

matriz = montaMatriz(l, c)

somas = []

x = 0
y = 0


for i in range(l):
    for j in range(c):
        soma = somaMatrizSec(x, y, l, c, m, n, matriz)
        y += 1
        somas.append(soma)
    x += 1

print(somas)