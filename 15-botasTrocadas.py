"""Botas Trocadas."""


def montaLista(n):
    """Monta lista de calcados."""
    calcados = []
    for i in range(n):
        entrada = input().split()
        calcados.append((int(entrada[0]), entrada[1]))
    return calcados


def minimo(x, y):
    """Retorna o minimo entre x e y."""
    if x <= y:
        return x
    elif y < x:
        return y


n = int(input())

calcados = montaLista(n)

pares = 0

for i in range(30, 61):
    d = 0
    e = 0
    for j in range(n):
        if calcados[j][0] == i and calcados[j][1] == 'E':
            e += 1
        elif calcados[j][0] == i and calcados[j][1] == 'D':
            d += 1

    pares += minimo(e, d)

print(pares)