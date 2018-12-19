"""Arvore Vermelha e Preta."""

from avlArvore import ArvoreAvl
from arvore import No


class ArvoreVP(ArvoreAvl):
    """Classe: Arvore Vermelha e Preta."""
    
    nil = No(None, None)
    nil.setDireito(None)
    nil.setEsquerdo(None)
    nil.setPai(None)

    def __init__(self):
        super().__int__()
        self.__raiz = self.nil

    def estaVazia(self):
        """Funçao sobrescrita."""
        if self.getRaiz() is self.nil:
            return True
        else:
            return False


arv = ArvoreVP()
#no = No(2,2)
#arv.insere(no)
print(arv.estaVazia())