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
    if somasLinhas[n-1] != somasLinhas[x]:
        linha = x
else:
    if somasColunas[n-1] != somasColunas[0] == somasColunas[1]:
        coluna = n-1
    if somasLinhas[n-1] != somasLinhas[0] == somasLinhas[1]:
        linha = n-1

valor = quadrado[linha][coluna]
colunaSemProb = None

if coluna != 0:
    colunaSemProb = 0
else:
    colunaSemProb = 1

diferenca = None

if somasColunas[colunaSemProb] < somasColunas[coluna]:
    diferenca = somasColunas[colunaSemProb] - somasColunas[coluna]
else:
    diferenca = somasColunas[coluna] - somasColunas[colunaSemProb]
    diferenca = abs(diferenca)

print(valor+diferenca, valor)