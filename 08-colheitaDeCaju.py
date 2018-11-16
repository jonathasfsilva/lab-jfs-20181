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


def somaMatriz2(x, y, m, n):
    fatias = []
    for i in range(y, y+m):
        try:
            fatia = matriz[i][x:x+n]
            if len(fatia) == n:
                fatias.append(sum(fatia))
        except:
            return sum(fatias)
    return sum(fatias)


l, c, m, n = input().split()
l, c, m, n = int(l), int(c), int(m), int(n)

matriz = montaMatriz(l, c)

x = 0
y = 0
maior = 0

for i in range(l-m+1):
    for j in range(c-n+1):
        soma = somaMatriz2(j, i, m, n)
        y += 1
        if soma > maior:
            maior = soma
    x += 1

print(maior)