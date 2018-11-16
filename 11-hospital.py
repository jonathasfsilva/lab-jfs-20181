"""Hospital."""


def ordenaGravidade(lista):
    """Ordena a gravidade."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j-1
        while i >= 0 and int(lista[i][1]) < int(chave[1]):
            lista[i+1] = lista[i]
            i -= 1
        lista[i+1] = chave
    return lista


def ordenaNome(lista):
    """Ordena os nomes com mesma gravidade."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j-1
        if int(lista[i][1]) == int(chave[1]):
            while i >= 0 and lista[i][0] > chave[0]:
                lista[i+1] = lista[i]
                i -= 1
            lista[i+1] = chave
    return lista


n = int(input())

premium, diamante, ouro, prata, bronze, resto = [], [], [], [], [], []


for x in range(n):
    nome, plano, gravidade = input().split()

    if plano == 'premium':
        premium.append((nome, int(gravidade)))
    elif plano == 'diamante':
        diamante.append((nome, int(gravidade)))
    elif plano == 'ouro':
        ouro.append((nome, int(gravidade)))
    elif plano == 'prata':
        prata.append((nome, int(gravidade)))
    elif plano == 'bronze':
        bronze.append((nome, int(gravidade)))
    else:
        resto.append((nome, int(gravidade)))

if len(premium) > 1:
    premium = ordenaNome(ordenaGravidade(premium))
if len(diamante) > 1:
    diamante = ordenaNome(ordenaGravidade(diamante))
if len(ouro) > 1:
    ouro = ordenaNome(ordenaGravidade(ouro))
if len(prata) > 1:
    prata = ordenaNome(ordenaGravidade(prata))
if len(bronze) > 1:
    bronze = ordenaNome(ordenaGravidade(bronze))
if len(resto) > 1:
    resto = ordenaNome(ordenaGravidade(resto))

for pessoa in premium:
    print(pessoa[0])
for pessoa in diamante:
    print(pessoa[0])
for pessoa in ouro:
    print(pessoa[0])
for pessoa in prata:
    print(pessoa[0])
for pessoa in bronze:
    print(pessoa[0])
for pessoa in resto:
    print(pessoa[0])