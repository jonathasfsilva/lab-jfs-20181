"""Edfd."""


def encontraPos(entrada, x, y):
    """DDD."""
    pos = 0
    if entrada == 'N':
        pos = (x, y)
    elif entrada == 'S':
        pos = (x, y)
    elif entrada == 'L':
        pos = (x, y)
    elif entrada == 'O':
        pos = (x, y)
    return pos


def orientacao(cmd, estado):
    """Altera a orientacao."""
    oriD = {'N': 'L', 'L': 'S', 'S': 'O', 'O': 'N'}
    oriE = {'N': 'O', 'O': 'S', 'S': 'L', 'L': 'S'}
    if cmd == 'D':
        estado = oriD[estado]
    elif cmd == 'E':
        estado = oriE[estado]
    return estado


def andar(estado, posicao, arena, n, m):
    """Andar."""
    linha = posicao[0]
    coluna = posicao[1]
    if estado == 'N' and linha - 1 > n:
        if arena[linha - 1][coluna] != '#':
            posicao = (linha - 1, coluna)
    elif estado == 'L' and coluna + 1 < m:
        if arena[linha][coluna + 1] != '#':
            posicao = (linha, coluna + 1)
    elif estado == 'S' and linha + 1 < n:
        if arena[linha + 1][coluna] != '#':
            posicao = (linha + 1, coluna)
    elif estado == 'O' and coluna - 1 > m:
        if arena[linha][coluna - 1] != '#':
            posicao = (linha, coluna - 1)
    return posicao


while True:
    estado = ''
    posicao = 0
    pontos = 0
    arena = []
    entrada = input().split()
    linha, coluna, acoes = entrada
    linha, coluna, acoes = int(linha), int(coluna), int(acoes)
    if linha == 0 and coluna == 0 and acoes == 0:
        break
    for i in range(linha):
        entrada = input()
        line = []
        for j in range(coluna):
            line.append(entrada[j])
            if not posicao != 0:
                posicao = encontraPos(entrada[j], i, j)
                estado = entrada[j]
        arena.append(line)
    comandos = input()

    for i in range(acoes):
        if comandos[i] == 'F':
            posicao = andar(estado, posicao, arena, linha, coluna)
        else:
            estado = orientacao(comandos[i], estado)
    print(posicao, estado)