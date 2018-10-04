u"""Robô Colecionador.

Lab
"""


class Arena:
    """Classe Arena."""

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

    def posAnteior(self):
        """Altera na Arena a posicao anterior."""
        # # BUG: NÃO TA FAZENDO MUDANÇA DE POSIÇÃO
        linha = self.posicao[0]
        coluna = self.posicao[1]
        Arena.ponto(linha, coluna)

    def posPosterior(self, posicao, estado):
        """Altera na Arena a posicao posterior ao movimento."""
        # # BUG: NÃO TA FAZENDO A MUDANÇA DE POSIÇÃO.
        linha = self.posicao[0]
        coluna = self.posicao[1]
        self.arena[linha][coluna] = estado

    def anda(self):
        """Faz andar."""
        if self.robo.estado == 'L':
            linha = self.robo.posicao[0]
            coluna = self.robo.posicao[1]
            self.robo.posicao = (linha + 1, coluna)
        elif self.robo.estado == 'N':
            linha = self.robo.posicao[0]
            coluna = self.robo.posicao[1]
            self.robo.posicao = (linha, coluna - 1)
        elif self.robo.estado == 'S':
            linha = self.robo.posicao[0]
            coluna = self.robo.posicao[1]
            self.robo.posicao = (linha, coluna + 1)
        elif self.robo.estado == 'O':
            linha = self.robo.posicao[0]
            coluna = self.robo.posicao[1]
            self.robo.posicao = (linha - 1, coluna)
