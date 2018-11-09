def gravidade(lista):
    u"""Ordena em função da gravidade."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j-1
        while i >= 0 and int(lista[i][2]) < int(chave[2]):
            lista[i+1] = lista[i]
            i -= 1
        lista[i+1] = chave


def alfabetica(lista):
    """Desempate em ordem alfabetica."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j-1
        if int(lista[i][2]) == int(chave[2]):
            while i >= 0 and lista[i][0] > chave[0]:
                lista[i+1] = lista[i]
                i -= 1
            lista[i+1] = chave


N = int(input())
premium, diamante, ouro, prata, bronze, resto = [], [], [], [], [], []
saida = []

for paciente in range(N):
    paciente = tuple(input().split(' '))
    if paciente[1] == 'premium':
        premium.append(paciente)
    elif paciente[1] == 'diamante':
        diamante.append(paciente)
    elif paciente[1] == 'ouro':
        ouro.append(paciente)
    elif paciente[1] == 'prata':
        prata.append(paciente)
    elif paciente[1] == 'bronze':
        bronze.append(paciente)
    elif paciente[1] == 'resto':
        resto.append(paciente)


gravidade(premium)
gravidade(diamante)
gravidade(ouro)
gravidade(prata)
gravidade(bronze)
gravidade(resto)

alfabetica(premium)
alfabetica(diamante)
alfabetica(ouro)
alfabetica(prata)
alfabetica(bronze)
alfabetica(resto)

saida.extend(premium)
saida.extend(diamante)
saida.extend(ouro)
saida.extend(prata)
saida.extend(bronze)
saida.extend(resto)


for s in saida:
    print(s[0])