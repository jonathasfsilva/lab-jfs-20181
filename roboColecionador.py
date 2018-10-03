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
        if self.estado == 'L':
            linha = self.posicao[0]
            coluna = self.posicao[1]
            self.posicao = (linha + 1, coluna)
        elif self.estado == 'N':
            linha = self.posicao[0]
            coluna = self.posicao[1]
            self.posicao = (linha, coluna - 1)
        elif self.estado == 'S':
            linha = self.posicao[0]
            coluna = self.posicao[1]
            self.posicao = (linha, coluna + 1)
        elif self.estado == 'O':
            linha = self.posicao[0]
            coluna = self.posicao[1]
            self.posicao = (linha - 1, coluna)


class Arena:
    """Classe Arena."""

    def __init__(self, linha, coluna, robo):
        """Construtor."""
        self.linha = int(linha)  # Linha
        self.coluna = int(coluna)  # Coluna
        self.robo = robo
        self.arena = []
        self.robo.posicao = 0
        for i in range(linha):
            entrada = input()
            line = []
            for j in range(coluna):
                line.append(entrada[j])
                if not self.robo.posicao != 0:
                    self.encontraPos(entrada[j], j, i)
            self.arena.append(line)

    def __repr__(self):
        """Plota arena."""
        plote = ''
        for i in self.arena:
            plote = plote + str(i) + '\n'
        return plote

    def encontraPos(self, entrada, x, y):
        """Enc."""
        j = y
        i = x
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
