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


def somaMatriz2(x, y, m, n, matriz):
    fatias = []
    for i in range(y, y+m):
        try:
            fatia = matriz[i][x:x+n]
            if len(fatia) == n:
                fatias.append(sum(fatia))
        except:
            return sum(fatias)
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
        soma = somaMatriz2(i, j, m, n, matriz)
        y += 1
        if soma != 0:
            somas.append(soma)
    x += 1

print(max(somas))