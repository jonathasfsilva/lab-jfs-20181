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

    def orientacao(self, cmd, estado):
        """Altera a orientacao."""
        oriD = {'N': 'L', 'L': 'S', 'S': 'O', 'O': 'N'}
        oriE = {'N': 'O', 'O': 'S', 'S': 'L', 'L': 'S'}

        if cmd == 'D':
            self.robo.estado = oriD[estado]
        elif cmd == 'E':
            self.robo.estado = oriE[estado]

    def anda(self):
        """Faz andar."""
        # falta implemetar


class Arena:
    """Classe Arena."""

    def __init__(self, n, m, robo):
        """Construtor."""
        self.n = int(n)
        self.m = int(m)
        self.robo = robo
        self.arena = []
        self.robo.posicao = 0
        for i in range(n):
            entrada = input()
            line = []
            for j in range(m):
                line.append(entrada[j])
                if not self.robo.posicao != 0:
                    Arena.encontraPos(entrada[j], j, i)
            self.arena.append(line)

    def __repr__(self):
        """Plota arena."""
        plote = ''

        # resolver como plotar o arena

        for i in range(self.arena):
            plote = plote + str(i) + '\n'
        return plote

    def encontraPos(self, entrada, x, y):
        """Encontra o robo."""
        j = x
        i = y

        if entrada == 'N':
            self.robo.posicao = (j, i)
            self.robo.estado = entrada
        elif entrada == 'S':
            self.robo.posicao = (j, i)
            self.robo.estado = entrada
        elif entrada == 'L':
            self.robo.posicao = (j, i)
            self.robo.estado = entrada
        elif entrada == 'S':
            self.robo.posicao = (j, i)
            self.robo.estado = entrada
