"""Quadrado."""

n = int(input())
quadrado = []
somasLinhas = []
somasColunas = []

for i in range(n):
    linha = []
    entrada = input().split()
    for j in range(n):
        linha.append(int(entrada[j]))
    quadrado.append(linha)

for x in range(len(quadrado)):
    somaLinha = 0
    somaColuna = 0
    for y in range(len(quadrado)):
        somaLinha += quadrado[x][y]
        somaColuna += quadrado[y][x]
    somasLinhas.append(somaLinha)
    somasColunas.append(somaColuna)

coluna = None
linha = None

for x in range(n-1):
    if somasColunas[n-1] != somasColunas[x]:
        coluna = x
        if x >= 1 and somasColunas[x] != somasColunas[0]:
            coluna = x + 1
    if somasLinhas[n-1] != somasLinhas[x]:
        linha = x
        if x >= 1 and somasLinhas[x] != somasLinhas[0]:
            linha = x + 1
else:
    if coluna == None:
        coluna = n-1
    if linha == None:
        linha = n-1

print(somasLinhas, somasColunas)
print(linha, coluna)