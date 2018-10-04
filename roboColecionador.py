"""RoboColecionador.

ex1 - Lab. 2018.2
Jonathas Felipe da Silva
"""


def encontraPos(entrada, x, y):
    """Encontra a posicao do robo."""
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
    oriE = {'N': 'O', 'O': 'S', 'S': 'L', 'L': 'N'}
    if cmd == 'D':
        estado = oriD[estado]
    elif cmd == 'E':
        estado = oriE[estado]
    return estado


def ponto(arena, posicao):
    """Bota o ponto na antiga posicao do robo."""
    linha = posicao[0]
    coluna = posicao[1]
    arena[linha][coluna] = '.'
    return arena


def lugar(arena, posicao, estado):
    """Bota o robo na nova posicao."""
    linha = posicao[0]
    coluna = posicao[1]
    arena[linha][coluna] = estado
    return arena


def andar(estado, posicao, arena, n, m):
    """Faz o robo andar."""
    linha = posicao[0]
    coluna = posicao[1]
    if estado == 'N' and (linha - 1) >= 0:
        if arena[linha - 1][coluna] != '#':
            posicao = (linha - 1, coluna)
    elif estado == 'L' and (coluna + 1) < m:
        if arena[linha][coluna + 1] != '#':
            posicao = (linha, coluna + 1)
    elif estado == 'S' and (linha + 1) < n:
        if arena[linha + 1][coluna] != '#':
            posicao = (linha + 1, coluna)
    elif estado == 'O' and (coluna - 1) >= 0:
        if arena[linha][coluna - 1] != '#':
            posicao = (linha, coluna - 1)
    return posicao


def pontua(arena, posicao, pontos):
    """Verifica se o robo pontuou."""
    linha = posicao[0]
    coluna = posicao[1]
    if arena[linha][coluna] == '*':
        pontos += 1
    return pontos


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
        arena = ponto(arena, posicao)
        if comandos[i] == 'F':
            posicao = andar(estado, posicao, arena, linha, coluna)
        else:
            estado = orientacao(comandos[i], estado)
        pontos = pontua(arena, posicao, pontos)
        arena = lugar(arena, posicao, estado)
    print(pontos)
