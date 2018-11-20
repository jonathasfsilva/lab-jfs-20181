"""Botas Trocadas."""
from time import time


def montaLista(n):
    """Monta lista de calcados"""
    calcados = []
    for i in range(n):
        entrada = input().split()
        calcados.append((int(entrada[0]), entrada[1]))
    return calcados


n = int(input())

calcados = montaLista(n)

ti = time()

pares = 0

for i in range(len(calcados)):
    for j in range(i, len(calcados)):
        if True:
            if calcados[j][0] == calcados[i][0] and calcados[i][1] != calcados[j][1]:
                pares += 1
                break

tf = time()
print(pares)
print(tf - ti)