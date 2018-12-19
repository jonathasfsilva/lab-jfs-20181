"""Arvore AVL.

    classe: ArvoreAvl()

    implementada por Jonathas F. Silva
"""


class No():
    """No basico para arvore binaria."""

    def __init__(self, dados):
        u"""Classe No é iniciada com: chave e dados.
        Atributos:
            pai - no pai
            chave - identificador de um objeto No, Tipo (inteiro)
            dados - informaçao armazenada nesse no.
            esquerdo - filho esquerdo
            direito - filho direito
        """
        self.__pai = None
        self.__chave = None
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


class ArvoreAvl():
    """Classe: Arvore AVL."""

    def __init__(self):
        """Construtor da arvore AVL."""
        self.__raiz = None

    def __repr__(self):
        """Plota o dado do no."""
        if not self.estaVazia():
            s = ''
            no = self.getRaiz()
            s += str(no.getPai()) + '\n'
            s += '^' + '\n'
            s += str(no.getEsquerdo()) + ' <- '
            s += str(no.getDado()) + ' -> '
            s += str(no.getDireito())
            return s
        else:
            return 'Esta vazia'

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
                return self.maximo(no.getEsquerdo())
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
        if self.getRaiz() is None:
            return True
        else:
            return False

    def busca(self, k):
        """Busca um no na arvore."""
        x = self.getRaiz()
        while x is not None and k != x.getDado():
            if k < x.getDado():
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
            if no.getDado() < x.getDado():
                x = x.getEsquerdo()
            else:
                x = x.getDireito()
        no.setPai(y)
        if y is None:
            self.setRaiz(no)
        elif no.getDado() < y.getDado():
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
            print(x.getDado(), end = ' ')
            self.emOrdem(x.getDireito())

    def preOrdem(self, x):
        """Plota a arvore em pre-ordem."""
        if x is not None:
            print(x.getDado(), end = ' ')
            self.preOrdem(x.getEsquerdo())
            self.preOrdem(x.getDireito())

    def posOrdem(self, x):
        """Plota a arvore em pos-ordem."""
        if x is not None:
            self.posOrdem(x.getEsquerdo())
            self.posOrdem(x.getDireito())
            print(x.getDado(), end = ' ')

    def maior(self, h1, h2):
        """Retorna o maximo da altura da arvore."""
        if h1 > h2:
            return h1+1
        else:
            return h2+1

    def altura(self, x):
        """Altura da arvore."""
        if x is None:
            return -1
        h1 = self.altura(x.getEsquerdo())
        h2 = self.altura(x.getDireito())
        return self.maior(h1, h2)

    def calFatorBalance(self, x):
        """Calcala o fator de balanceamento das subarvores."""
        esq = x.getEsquerdo()
        dir = x.getDireito()
        return self.altura(esq) - self.altura(dir)

    def rotaEsquerda(self, x):
        """Rotaçao simples a esquerda."""
        y = x.getDireito()
        x.setDireito(y.getEsquerdo())
        y.getEsquerdo().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() is None:
            self.setRaiz(y)
        elif x is x.getPai().getEsquerdo():
            x.getEsquerdo().setPai(y)
        else:
            x.getDireito().setPai(y)
        y.setEsquerdo(x)
        x.setPai(y)

    def rotaDireita(self, x):
        """Rotaçao simples a direita."""
        y = x.getEsquerdo()
        x.setEsquerdo(y.getDireito())
        y.getDireito().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() is None:
            self.setRaiz(y)
        elif x is x.getPai().getDireito():
            x.getDireito().setPai(y)
        else:
            x.getEsquerdo().setPai(y)
        y.setDireito(x)
        x.setPai(y)

    def rotaEsquerdaDupla(self, x):
        """Rotaçao dupla a esquerda"""
        self.rotaEsquerda(x.getEsquerdo())
        self.rotaDireita(x.getPai())

    def rotaDireitaDupla(self, x):
        """Rotacao dupla a direita."""
        self.rotaDireita(x.getDireito)
        self.rotaEsquerda(x.getPai())

    def rebalanca(self, x):
        balanco = self.calFatorBalance(x)

        if balanco > 1:
            if x.getEsquerda().calFatorBalanc() > 0:



arv = ArvoreAvl()
arv.insere(No(2))
arv.insere(No(3))
print(arv)