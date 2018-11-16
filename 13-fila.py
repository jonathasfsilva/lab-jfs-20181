"""Ninguem aguenta mais fila."""


class No:
    """Classe No."""

    def __init__(self, dado):
        """Construtor do No."""
        self._dado = dado
        self._proxNo = None

    def getDado(self):
        """Retorna o dado do no."""
        return self._dado

    def setDado(self, dado):
        """Seta o novo dado."""
        self._dado = dado

    def getProxNo(self):
        """Retorna a referencia do proximo no"""
        return self._proxNo

    def setProxNo(self, novoNo):
        """Seta o novo no."""
        self._proxNo = novoNo


class Lista:
    """Classe Lista encadeada."""

    def __init__(self):
        """Construtor da lista."""
        self._primeiroNo = None
        self._ultimoNo = None

    def __str__(self):
        """Plota a lista."""
        if self.estaVazia():
            return 'A lista esta vazia.'
        noAtual = self._primeiroNo
        string = ''
        while noAtual is not None:
            string += str(noAtual.getDado()) + ' '
            noAtual = noAtual.getProxNo()
        return string

    def inserirInicio(self, valor):
        """Insere no inicio da lista."""
        novoNo = No(valor)
        if self.estaVazia():
            self._primeiroNo = self._ultimoNo = novoNo
        else:
            novoNo.setProxNo(self._primeiroNo)
            self._primeiroNo = novoNo

    def inserirFinal(self, valor):
        """Insere no final da lista"""
        novoNo = No(valor)
        if self.estaVazia():
            self._primeiroNo = self._ultimoNo = novoNo
        else:
            self._ultimoNo.setProxNo(novoNo)
            self._ultimoNo = novoNo

    def removerInicio(self):
        """Remove no inicial da lista."""
        if self.estaVazia():
            raise ImportError
        primeiroNoValor = self._primeiroNo.getDado()
        if self._primeiroNo is self._ultimoNo:
            self._primeiroNo = None
            self._ultimoNo = None
        else:
            self._primeiroNo = self._primeiroNo.getProxNo()
        return primeiroNoValor

    def removerFinal(self):
        """Remove o ultimo no da lista"""
        if self.estaVazia():
            raise IndexError
        ultimoNoValor = self._ultimoNo.getDado()
        if self._primeiroNo is self._ultimoNo:
            self._primeiroNo = None
            self._ultimoNo = None
        else:
            noAtual = self._primeiroNo
            while noAtual.getProxNo() is not self._ultimoNo:
                noAtual = noAtual.getProxNo()
            noAtual.setProxNo(None)
            self._ultimoNo = noAtual
        return ultimoNoValor

    def estaVazia(self):
        """Lista vazia, True ou False"""
        return self._primeiroNo is None


class Fila(Lista):
    """Classe fila."""
    def novaPessoa(self, dado):
        if self.estaVazia():
            self.inserirInicio(dado)
        else:
            self.inserirFinal(dado)

    def removePessoa(self, dado):
        if self.estaVazia():
            return ''
        if fila._primeiroNo.getDado() == dado:
            fila.removerInicio()
        elif fila._ultimoNo.getDado() == dado:
            fila.removerFinal()
        else:
            atual = self._primeiroNo
            while atual.getProxNo() is not None:
                if atual.getProxNo().getDado() == dado:
                    proximo = atual.getProxNo().getProxNo()
                    atual.setProxNo(proximo)
                atual = atual.getProxNo()


n = int(input())

filaIncial = input().split()

m = int(input())

filaSairam = input().split()

fila = Fila()

for i in range(n):
    fila.novaPessoa(filaIncial[i])


for j in range(m):
    fila.removePessoa(filaSairam[j])

print(fila)