"""Juvenal nao quer lavar louca."""

from lista_encadeada import Lista

class Fila(Lista):
    """Classe fila."""

    def inserirCarta(self, dado):
        """Insere carta."""
        if self.estaVazia():
            self.inserirInicio(dado)
        else:
            self.inserirFinal(dado)

def verifica(lista):
    return 0


f = int(input())

for i in range(f):
    entrada = input().split()

    mesa = Fila() # Deck

    for carta in entrada:
        mesa.inserirCarta(carta)

    print(mesa)

    while True:
        entrada = input().split()

        if entrada[0] == -1 and len(entrada) == 1:
            break
        else:
            noAtual = mesa._primeiroNo
            while noAtual is not None:
                if noAtual.getDado() is entrada:
                    print('entrou')