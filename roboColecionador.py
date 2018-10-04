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
            x = posicao[0]
            y = posicao[1]
            arena[posicao[0]][posicao[1]] = '.'
            if estado == 'N' and (x - 1) >= 0 and arena[x-1][y] != '#':
                posicao = ((x-1), y)
            elif estado == 'L' and (y + 1) < coluna and arena[x][y + 1] != '#':
                posicao = (x, y + 1)
            elif estado == 'S' and (x + 1) < linha and arena[x+1][y] != '#':
                posicao = (x + 1, y)
            elif estado == 'O' and (y - 1) >= 0 and arena[x][y-1] != '#':
                posicao = (x, y - 1)
            x = posicao[0]
            y = posicao[1]
            if arena[x][y] == '*':
                pontos += 1
            arena[x][y] = estado
        else:
            estado = orientacao(comandos[i], estado)

    print(pontos)
