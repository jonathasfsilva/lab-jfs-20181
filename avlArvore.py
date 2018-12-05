"""Arvore AVL.

    classe: ArvoreAvl(Arvore)

    implementada por Jonathas F. Silva
"""

from arvore import No
from arvore import Arvore


class ArvoreAvl(Arvore):
    """Classe: Arvore AVL."""

    nil = No(None, None)
    nil.setPai(None)
    nil.setEsquerdo(None)
    nil.setDireito(None)

    def __init__(self):
        """Construtor da arvore AVL."""
        super().__init__()
        self.__raiz = None
        self.__esquerdo = self.nil
        self.__direito = self.nil

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
        self.rotaEsquerda(x)
        self.rotaDireita(x.getPai())



lll = [3,0,6,1,5,-30,55,-25,50,-10,99,100,101,102]

ll = [3, 2, 4]

l = [30, 10, 20]

dado = 'bsi'
arv = ArvoreAvl()

for i in l:
    no = No(i, str(i))
    arv.insere(no)

arv.getRaiz()
print(arv.getRaiz())


arv.getRaiz()
arv.emOrdem(arv.getRaiz())
print()
arv.rotaEsquerdaDupla(arv.busca(10))