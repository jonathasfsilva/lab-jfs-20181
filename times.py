"""Times."""


def quickSort(lista):
    """QuickSort.

    Recebe uma lista e retorna ela ordenada por QuickSort.
    """
    if len(lista) <= 1:
        return lista
    less, equal, greater = [], [], []
    pivot = lista[0]
    for x in lista:
        # ORDEM ALFABETICA
        if x[0] < pivot[0]:
            less.append(x)
        elif x[0] == pivot[0]:
            equal.append(x)
        else:
            greater.append(x)
    return quickSort(less) + equal + quickSort(greater)


def quickSort2(lista):
    """QuickSort.

    Recebe uma lista e retorna ela ordenada por QuickSort.
    """
    if len(lista) <= 1:
        return lista
    less, equal, greater = [], [], []
    pivot = lista[0]
    for x in lista:
        # ORDEM POR HABILIDADE
        if x[1] > pivot[1]:
            greater.append(x)
        elif x[1] == pivot[1]:
            equal.append(x)
        else:
            less.append(x)
    return quickSort2(greater) + equal + quickSort2(less)


n, t = input().split()

jogadores, times = [], []

for i in range(int(n)):
    nome, habilidade = input().split()
    jogadores.append((nome, int(habilidade)))

# Ordena jogadores
jogadores = quickSort2(jogadores)

for i in range(int(t)):
    # Cria os times
    times.append([])

for i in range(int(n)):
    # Bota os jogadores nos times
    times[i % int(t)].append(jogadores[i])

for i in range(int(t)):
    # Ordena os jogadores nos times em ordem alfabetica
    times[i] = quickSort(times[i])

for time in range(len(times)):
    # plota a saida
    print('Time', time+1)
    for i in range(len(times[time])):
        print(times[time][i][0])
    print()