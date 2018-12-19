n, inicio, chegada = input().split()

lista = [[] for x in range(int(n))]

while True:
    entrada = input()
    if entrada == '':
        break
    else:
        a, b = entrada.split()
        a, b = int(a)-1, int(b)-1
        lista[a].append(b)
        lista[b].append(a)


def procura(lista, atual, chegada, anterior, contador):
    if atual == chegada:
        print(contador)
        return
    else:
        for j in lista[atual]:
            if j != anterior:
                procura(lista, j, chegada, atual, contador+1)


procura(lista, int(inicio), int(chegada), None, 0)