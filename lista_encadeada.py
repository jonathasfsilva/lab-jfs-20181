"""Lista puplamente encadeada"""


class ListaDuplamenteEncadeada():

    def __init__(self, inicio = None):
        self._inicio = inicio

    def __str__(self):
        s = ''
        i = self._inicio
        while i is not None:
            s += " "+i.getDado()
        return s

    def getProx(self):
        return self._prox

    def setProx(self, dado):
        self._prox = dado

    def getAnt(self):
        return self._ant

    def setAnt(self, dado):
        self._ant = dado

    def getIncio(self):
        return self._inicio

    def setInicio(self, inicio):
        self._inicio = inicio

    def isVazia(self):
        return self._inicio == None

    def inserirNoInicio(self, dado):
        novono = No(dado)
        if not self.isVazia():
            novono.setProx(self._inicio)
            self._inicio.setAnt(novono)
        self._inicio = novono

    def buscar(self, dado):
        i = self._inicio
        while i != None or i.getDado() != dado:
            i = i.getProx()
        return i

    def remover(self, dado):
        i = self.buscar(dado)

        if i is not None:
            if i is not self._inicio:
                i.getProx().setAnt(i.getAnt())
            if i.getProx is not None:
                i.getAnt().setProx(i.getProx())

    def removerDoInicio(self):
        i = self._inicio
        if i is not None:
            if self._inicio.getProx() is not None:
               self._inicio.getProx().setAnt(None)
            self._inicio = self._inicio.getProx()
        return i


class Fila(ListaDuplamenteEncadeada):

    def __init__(self, inicio, fim):
        super(Fila).__init__(inicio)
        self._fim = fim

    def removerDoFim(self):
        if self._fim is not None:
            if self._fim.getAnt() is not None:
                self._fim.getAnt().setProx(None)
            self._fim = None
        return self._fim


class Pilha(ListaDuplamenteEncadeada):
    def push(self, dado):
        self.inserirNoInicio(dado)

    def pop(self):
        return self.removerDoInicio()