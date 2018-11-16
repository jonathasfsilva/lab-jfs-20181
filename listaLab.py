class No:
    def __init__(self, dado, prox=None, ant=None):
        self._dado = dado
        self._prox = prox
        self._ant = ant

    def getDado(self):  # so precisa desses sets  (altera o valor da variável) e gets (retorna o valor da variável) pois estão privados
        return self._dado

    def setDado(self, dado):
        self._dado = dado

    def getProx(self):
        return self._prox

    def setProx(self, prox):
        self._prox = prox

    def getAnt(self):
        return self._ant

    def setAnt(self, ant):
        self._ant = ant


class ListaDuplamenteEncadeada:
    def __init__(self, inicio=None):
        self._inicio = inicio

    def getInicio(self):
        return self._inicio

    def setInicio(self, inicio):
        self._inicio = inicio

    def isVazia(self):
        return self.inicio == None  # retorna se a lista está vazia (True) ou não vazia (false)

    def inserirNoInicio(self, dado):
        novono = No(dado)
        if not self.isVazia():
            novono.setProx(self._inicio)
            self._inicio.setAnt(novono)
        self._inicio = novono

    def buscar(self, dado):
        i = self._inicio  # vai varrer
        while i != None or i.getDado() != dado:
            i = i.getProx()
        return i

    def removerDoInicio(self, dado):
        i = self.buscar(dado)
        if i is not None:
            if self._inicio.getProx() is not None:
                self._inicio.getProx().setAnt(None)
            self._inicio = self._inicio.getProx()
        return i  # traz o nó

    def __str__(self):
        s = ""
        i = self._inicio
        while i is not None:
            s += " " + i.getDado()
        return s


class Fila(ListaDuplamenteEncadeada):
    def __init__(self, inicio=None, fim=None):
        super(Fila).__init__(inicio)
        self._fim = fim

    def removerDoFim(self):
        fim = self._fim
        if fim is not None:
            if fim.getAnt() is not None:
                fim.getAnt().setProx(None)
            self._fim = fim.getAnt()
        return fim


class Pilha(ListaDuplamenteEncadeada):
    def push(self, dado):
        self.inserirNoInicio(dado)

    def pop(self):
        return self.removerDoInicio()


fila = Fila()
valores = [1, 2, 34, 2]
for i in valores:
    fila.inserirNoInicio(i)
print(Fila)

# if not self.isVazia():
#   if self._fim.getAnt() is not None:
#      self._fim.getAnt().setProx(None)

