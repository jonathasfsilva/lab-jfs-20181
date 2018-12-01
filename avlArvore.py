from arvore import No
from arvore import Arvore


class ArvoreAvl(Arvore):
    """Classe: Arvore AVL."""

    nil = No(None, None)
    nil.setPai(None)
    nil.setDireito(None)
    nil.setEsquerdo(None)

    def __init__(self):
        """Construtor da arvore AVL."""
        super().__init__()
        self.__raiz = self.nil

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

    def insere(self, no):
        """Insere um No na arvore."""
        y = self.nil
        x = self.getRaiz()
        while x is not self.nil:
            y = x
            if no.getChave() < x.getChave():
                x = x.getEsquerdo()
            else:
                x = x.getDireito()
        no.setPai(y)
        if y is self.nil:
            self.setRaiz(no)
        elif no.getChave() < y.getChave():
            y.setEsquerdo(no)
        else:
            y.setDireito(no)

    def rotaEsquerda(self, x):
        """Rotaçao simples a esquerda."""
        y = x.getDireito()
        x.setDireito(y.getEsquerdo())
        y.getEsquerdo().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() is self.nil:
            self.setRaiz(y)
        elif x is x.getPai().getEsquerdo():
            x.getEsquerdo().setPai(y)
        else:
            x.getDireito().setPai(y)
        y.setEsquerdo(x)
        x.setPai(y)



ll = [3,0,6,1,5,-30,55,-25,50,-10,99]

l = [3, 2, 1]

dado = 'bsi'
arv = ArvoreAvl()

for i in l:
    no = No(i, str(i))
    arv.insere(no)

arv.emOrdem(arv.getRaiz())
print()
print('raiz -', arv.getRaiz().getDado())
# arv.rotaEsquerda(arv.getRaiz())

# FALTA FAZER COM QUE OS NOS FOLHAS APONTEM PRA O NIL.
