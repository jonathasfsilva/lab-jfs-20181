"""Arvore de busca binaria.

    classes: No, Arvore

    implementada por Jonathas F. Silva
"""

class No():
    """No basico para arvore binaria."""

    def __init__(self, chave, dados):
        u"""Classe No é iniciada com: chave e dados.
        Atributos:
            pai - no pai
            chave - identificador de um objeto No, Tipo (inteiro)
            dados - informaçao armazenada nesse no.
            esquerdo - filho esquerdo
            direito - filho direito
        """
        self.__pai = None
        self.__chave = chave
        self.__dado = dados
        self.__esquerdo = None
        self.__direito = None

    def __repr__(self):
        """Plota o dado do no."""
        return self.__dado

    def getPai(self):
        """Retorna no pai."""
        return self.__pai

    def setPai(self, pai):
        """Define no pai."""
        self.__pai = pai

    def getChave(self):
        """Retorna a chave de acesso."""
        return self.__chave

    def setChave(self, chave):
        """Define um nova chave."""
        self.__chave = chave

    def getDado(self):
        """Retorna o dado do no."""
        return self.__dado

    def setDado(self, dado):
        """Define o dado do no."""
        self.__dado = dado

    def getEsquerdo(self):
        """Retorna o filho esquerdo."""
        return self.__esquerdo

    def setEsquerdo(self, esquerdo):
        """Define o filho esquerdo."""
        self.__esquerdo = esquerdo

    def getDireito(self):
        """Retorna o filho direito."""
        return self.__direito

    def setDireito(self, direito):
        """Define o filho direito."""
        self.__direito = direito


class Arvore():
    """Arvore de busca binaria."""

    def __init__(self):
        """Contrutor da arvore."""
        self.__raiz = None

    def __repr__(self):
        """Plota o dado do no."""
        s = ''
        no = self.getRaiz()
        s += str(no.getPai()) + '\n'
        s += '^' + '\n'
        s += str(no.getEsquerdo()) + ' <- '
        s += str(no.getDado()) + ' -> '
        s += str(no.getDireito())
        return s

    def getRaiz(self):
        """Retorna a raiz da arvore."""
        return self.__raiz

    def setRaiz(self, raiz):
        """Define raiz da arvore."""
        self.__raiz = raiz

    def minimo(self, no):
        """Retorna o minimo da arvore."""
        if no is not None:
            while no.getEsquerdo() is not None:
                no = no.getEsquerdo()
            return no

    def maximo(self, no):
        """Retorna o maximo da arvore."""
        if no is not None:
            while no.getDireito() is not None:
                no = no.getDireito()
            return no

    def antecessor(self, no):
        """Retorna o antecessor do no."""
        if no is not None:
            if no.getEsquerdo() is not None:
                return self.maximo(no.getEsquerdo)
            else:
                pai = no.getPai()
                while pai is not None and no is pai.getEsquerdo():
                    no = pai
                    pai = no.getPai()
                    return pai

    def sucessor(self, no):
        """Retorna o sucessor do no."""
        if no is not None:
            if no.getDireito() is not None:
                return self.minimo(no.getDireito())
            else:
                pai = no.getPai()
                while pai is not None and no is pai.getDireito():
                    no = pai
                    pai = no.getPai()
                    return pai

    def estaVazia(self):
        """Retorna True se esta vazia e False se estiver vazia."""
        if self.getRaiz() is not None:
            return True
        else:
            return False

    def busca(self, k):
        """Busca um no na arvore."""
        x = self.getRaiz()
        while x is not None and k != x.getChave():
            if k < x.getChave():
                x = x.getEsquerdo()
            else:
                x = x.getDireito()
        return x

    def insere(self, no):
        """Insere um No na arvore."""
        y = None
        x = self.getRaiz()
        while x is not None:
            y = x
            if no.getChave() < x.getChave():
                x = x.getEsquerdo()
            else:
                x = x.getDireito()
        no.setPai(y)
        if y is None:
            self.setRaiz(no)
        elif no.getChave() < y.getChave():
            y.setEsquerdo(no)
        else:
            y.setDireito(no)

    def remove(self, z):
        """Remove um no da arvore."""
        if (z.getEsquerdo() is None) or (z.getDireito() is None):
            y = z
        else:
            y = self.sucessor(z)
        if y.getEsquerdo() is not None:
            x = y.getDireito()
        else:
            x = y.getDireito()
        if x is not None:
            x.setPai(y.getPai())
        if y.getPai() is None:
            self.setRaiz(x)
        else:
            if y == y.getPai().getEsquerdo():
                y.getPai().setEsquerdo(x)
            else:
                y.getPai().setDireito(x)

        if y != z:
            z.setChave(y.getChave())
        return y

    def emOrdem(self, x):
        """Plota a arvore em ordem."""
        if x is not None:
            self.emOrdem(x.getEsquerdo())
            print(x.getChave(), end = '')
            self.emOrdem(x.getDireito())

    def preOrdem(self, x):
        """Plota a arvore em pre-ordem."""
        if x is not None:
            print(x.getChave(), end = ' ')
            self.preOrdem(x.getEsquerdo())
            self.preOrdem(x.getDireito())

    def posOrdem(self, x):
        """Plota a arvore em pos-ordem."""
        if x is not None:
            self.posOrdem(x.getEsquerdo())
            self.posOrdem(x.getDireito())
            print(x.getChave(), end = ' ')
