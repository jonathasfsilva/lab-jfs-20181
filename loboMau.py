"""O lobo mau e as ovelhas do Juvenal."""


def pegaPosicoes(animal, i, j):
    if animal == 'v':
        posLobo.append((i, j))
    elif animal == 'k':
        posOvelha.append((i, j))


def montaPasto(m, n):
    """Monta matriz pasto."""
    pasto = []
    for i in range(m):
        linha = []
        entrada = input()
        for j in range(n):
            linha.append(entrada[j])
            if entrada[j] == 'k' or entrada[j] == 'v':
                pegaPosicoes(entrada[j], i, j)
        pasto.append(linha)
    return pasto


def explorar(lobo):
    if



m, n = input().split()
m, n = int(m), int(n)

posLobo = []

posOvelha = []

pasto = montaPasto(m, n)

print(posOvelha)
print(posLobo)