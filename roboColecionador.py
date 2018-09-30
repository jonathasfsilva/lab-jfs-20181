u"""Robô Colecionador.

Lab
"""


class Robo:
    """Classe Robo."""

    def __init__(self, posicao, estado, pontos):
        """Construtor."""
        self.posicao = posicao
        self.estado = estado
        self.pontos = pontos

    def __repr__(self):
        """Retorna estado do robo."""
        return str(self.estado)

    def orientacao(posicao, cmd, estado):
        """Altera a orientacao."""
        if estado == 'N':
            if cmd == 'E':
                estado = 'O'
            elif cmd == 'D':
                estado = 'L'
        elif estado == 'S':
            if cmd == 'D':
                estado = 'O'
            elif cmd == 'E':
                estado = 'L'
        elif estado == 'L':
            if cmd == 'D':
                estado = 'N'
            elif cmd == 'E':
                estado = 'S'
        elif estado == 'O':
            if cmd == 'E':
                estado = 'N'
            elif cmd == 'D':
                estado == 'S'


class Arena:
    """Classe Arena."""

    def __init__(self, n, m, robo):
        """Construtor."""
        self.n = int(n)
        self.m = int(m)
        self.robo = robo

    def __repr__(self):
        """Plota arena."""
        plote = ''

        # resolver como plotar o arena

        #  for i in range(self.arena):
        #    plote = plote + str(i) + '\n'
        return plote

    def encontraPos(entrada, x, y, posicao):
        """Encontra o robo."""
        j = x
        i = y

        if entrada == 'N':
            posicao = (j, i)
        elif entrada == 'S':
            posicao = (j, i)
        elif entrada == 'L':
            posicao = (j, i)
        elif entrada == 'S':
            posicao = (j, i)
        return posicao


def criaArena():
    """Cria Arena."""
    linha = input().split()
    n, m, s = linha
    n, m, s = int(n), int(m), int(s)
    arena = []
    posicao = 0

    for i in range(n):
        entrada = input()
        line = []
        for j in range(m):
            line.append(entrada[j])
            if not posicao != 0:
                # posicao já encontrada, não precisa mais procurar.
                # lembrar de zerar no proximo loop.
                posicao = Arena.encontraPos(entrada[j], j, i, posicao)
        arena.append(line)
