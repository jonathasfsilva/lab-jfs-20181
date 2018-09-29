u"""Robô Colecionador.

Lab
"""

posicao = 0


class Robo:
    """Classe Robo."""

    def __init__(self, posicao, estado, pontos):
        """Construtor."""
        self.posicao = posicao
        self.estado = estado
        self.pontos = pontos

    def __repr__(self):
        """Plota objeto."""
        return str(self.posicao)

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


class Campo:
    """Classe Campo."""

    def __init__(self, n, m, campo, robo):
        """Construtor."""
        self.n = n
        self.m = m
        self.campo = campo
        self.robo = robo

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


linha = input().split()
n, m, s = linha
n, m, s = int(n), int(m), int(s)
campo = []



def criaCampo(n, m):
    """Criacampo."""
    for i in range(n):
        entrada = input()
        line = []
        for j in range(m):
            line.append(entrada[j])
            if not posicao != 0:
                # posicao já encontrada, não precisa mais procurar.
                # lembrar de zerar no proximo loop.
                posicao = Campo.encontraPos(entrada[j], j, i, posicao)
        campo.append(line)
    camp = Campo(n, m, campo, a)






a = Robo(posicao, 'N', 0)
print(a)
