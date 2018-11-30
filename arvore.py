class Node():
    u"""Unidade básica para funcionamento da Árvore Binária."""

    def __init__(self, key, data):
        u"""Classe Node é iniciada com argumentos key e data.
        Argumentos:
            key  - identificador de um objeto Node. Tipo - Inteiro.
            data - informação armazenada pelo objeto Node.
        Atributos:
            left   - filho esquerdo
            right  - filho direito
            parent - nó pai
        """
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def getKey(self):
        """Retorna chave de acesso."""
        return self.key

    def getData(self):
        u"""Retorna conteúdo armazenado."""
        return self.data

    def getLeft(self):
        """Retorna filho esquerdo."""
        return self.left

    def getRight(self):
        """Retorna filho direito."""
        return self.right

    def getParent(self):
        u"""Retorna nó pai."""
        return self.parent

    def setKey(self, key):
        """Define chave de acesso."""
        self.key = key

    def setData(self, data):
        u"""Define conteúdo armazenado."""
        self.data = data

    def setLeft(self, left):
        """Define filho esquerdo."""
        self.left = left

    def setRight(self, right):
        """Define filho direito."""
        self.right = right

    def setParent(self, parent):
        u"""Define nó pai."""
        self.parent = parent

    def __repr__(self):
        return self.getData()


class Tree():
    u"""Árvore de Busca Binária."""

    def __init__(self):
        u"""
        Inicia a Árvore com um objeto Node como raiz.
        t = Tree(Node(1,"a"))
        """
        self.root = None

    def setRoot(self, root):
        self.root = root

    def minimum(self, x):
        if x is not None:
            while x.getLeft() is not None:
                x = x.getLeft()
            return x.getData()

    def maximum(self, x):
        if x is not None:
            while x.getRight() is not None:
                x = x.getRight()
            return x.getData()

    def successor(self, x):
        if x is not None:
            if x.getRight() is not None:
                return self.minimum(x.getRight())
            else:
                father = x.getParent()
                while father is not None and x is father.getRight():
                    x = father
                    father = x.getParent()
                    return father

    def antecessor(self, x):
        if x.getLeft() is not None:
            return self.maximum(x.getLeft())
        y = x.getParent()
        while (y is not None) and (x == y.getLeft()):
            x = y
            y = y.getParent()
            return y

    def insert(self, z):
        u"""Insere um objeto Node na árvore."""
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.getKey() < x.getKey():
                x = x.getLeft()
            else:
                x = x.getRight()
        z.setParent(y)
        if y is None:
            self.root = z
        elif z.getKey() < y.getKey():
            y.setLeft(z)
        else:
            y.setRight(z)

    def delete(self, z):
        if (z.getLeft() is None) or (z.getRight() is None):
            y = z
        else:
            y = z.successor()
        if y.getLeft() is not None:
            x = y.getLeft()
        else:
            x = y.getRight()
        if x is not None:
            x.setParent(y.getParent())
        if y.getParent() is None:
            self.root = x
        else:
            if y == y.getParent().getLeft():
                y.getParent().setLeft(x)
            else:
                y.getParent().setRight(x)

        if y != z:
            z.setKey(y.getKey())
        # print(y.getKey())

    def preOrderTreeWalk(self, x):
        if x is not None:
            print(x.getKey(), end = " ")
            self.preOrderTreeWalk(x.getLeft())
            self.preOrderTreeWalk(x.getRight())

    def inOrderTreeWalk(self, x):
        if x is not None:
            self.inOrderTreeWalk(x.getLeft())
            print(x.getData(), end = " ")
            self.inOrderTreeWalk(x.getRight())

    def postOrderTreeWalk(self, x):
        if x is not None:
            self.postOrderTreeWalk(x.getLeft())
            self.postOrderTreeWalk(x.getRight())
            print(x.getKey(), end = " ")

    def search(self, k):
        x = self.root
        while x is not None and k != x.getKey():
            if k < x.getKey():
                x = x.getLeft()
            else:
                x = x.getRight()
        return x

    def populate(self, first, last):
        self.raiz = Node(last//2, None)
        for i in range((last//2)-1, first-1, -1):
            self.inserir(i)
        for i in range((last//2) + 1, last+1):
            self.inserir(i)


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
            while no.getDado() is not None:
                no = no.getEsquerdo()
            return no.getDado()

    def maximo(self, no):
        """Retorna o maximo da arvore."""
        if no is not None:
            while no.getDado is not No:
                no = no.getDireito()
            return no.getDado()

    def estaVazia(self):
        """Retorna True se esta vazia e False se estiver vazia."""
        if self.getRaiz() is not None:
            return True
        else:
            return False

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

    def emOrdem(self, x):
        """Plota a arvore em ordem."""
        if x is not None:
            self.emOrdem(x.getEsquerdo())
            print(x.getChave(), end = ' ')
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

l = [3,2,1,4,6,0,10,55]
dado = 'bsi'
arv = Arvore()

for i in l:
    no = No(i, str(i))
    arv.insere(no)

arv.emOrdem(arv.getRaiz())

