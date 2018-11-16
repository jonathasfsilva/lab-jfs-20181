"""Expressoes."""

"""Lista encadeada."""


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


class Node:
    """Classe que define um nodo simples de uma Estrutura de dados: (info, NextNodo)"""

    def __init__(self, data):
        """Construtor do Nodo"""
        self.data = data
        self.nextNode = None

    def getData(self):
        """Retorna o Dado armazenado no nodo"""
        return self.data

    def setData(self, data):
        """Atribui valor ao Dado do nodo"""
        self.data = data

    def getNextNode(self):
        """Retorna a referencia do proximo nodo"""
        return self.nextNode

    def setNextNode(self, newNode):
        """Ajusta a referencia do proximo nodo"""
        self.nextNode = newNode;


class List:
    """Classe para uma Lista Encadeada:
            Esta classe tem dois ponteiros:
                firstNode: aponta para o primeiro nodo da lista
                lastNode: aponta para o ultimo nodo da lista
            Ao iniciar a lista ambos os ponteiros apontam para NULO"""

    def __init__(self):
        """Construtor da Lista"""
        self.firstNode = None
        self.lastNode = None

    def __str__(self):
        """Override do Estatuto STRING"""
        if self.isEmpty():
            return "A lista esta vazia!"
        correntNode = self.firstNode
        string = "A lista eh:"
        while correntNode is not None:
            string += str(correntNode.getData()) + " "
            correntNode = correntNode.getNextNode()
        return string

    def insertAtBegin(self, value):
        """Insere elemento no Inicio da lista"""
        newNode = Node(value)  # instancia de um novo nodo
        if self.isEmpty():  # Insersao para Lista vazia
            self.firstNode = self.lastNode = newNode
        else:  # Insersao para lista nao vazia
            newNode.setNextNode(self.firstNode)
            self.firstNode = newNode

    def insertAtEnd(self, value):
        """Insere emento no inicio da lista"""
        newNode = Node(value)  # instancia de um novo nodo

        if self.isEmpty():  # Se a lista esta vazia
            self.firstNode = self.lastNode = newNode
        else:
            self.lastNode.setNextNode(newNode)
            self.lastNode = newNode

    def removeFromBegin(self):
        """Remove o nodo inicial da lista"""
        if self.isEmpty():
            raise IndexError  # Remossao de uma Lista Vazia
        firstNodeValue = self.firstNode.getData()
        if self.firstNode is self.lastNode:
            self.firstNode = self.lastNode = None
        else:
            self.firstNode = self.firstNode.getNextNode()
        return firstNodeValue

    def removeFromEnd(self):
        """Remove o ultimo nodo da lista"""
        if self.isEmpty():
            raise IndexError  # Remocao de lista vazia!
        lastNodeValue = self.lastNode.getData()
        if self.firstNode is self.lastNode:
            self.firstNode = self.lastNode = None
        else:
            currentNode = self.firstNode
            while currentNode.getNextNode() is not self.lastNode:
                currentNode = currentNode.getNextNode()
            currentNode.setNextNode(None)
            self.lastNode = currentNode
        return lastNodeValue

    def isEmpty(self):
        """A lista esta vazia? True or False"""
        return self.firstNode is None


class Pilha(List):
    """Classe pilha"""
    def push(self, dado):
        self.insertAtBegin(dado)

    def pop(self):
        return self.removeFromBegin()


def verifica(expressao):
    pilha = Pilha()
    try:
        for carac in expressao:
            if carac == '(':
                pilha.push(carac)
            elif carac == '{':
                pilha.push(carac)
            elif carac == '[':
                pilha.push(carac)
            elif carac == ')' and pilha.firstNode.getData() == '(':
                pilha.pop()
            elif carac == ']' and pilha.firstNode.getData() == '[':
                pilha.pop()
            elif carac == '}' and pilha.firstNode.getData() == '{':
                pilha.pop()
        if pilha.isEmpty():
            return True
        else:
            return False
    except:
        return False


n = int(input())
resultados = []

for i in range(n):
    expressao = input()
    if verifica(expressao):
        resultados.append('S')
    else:
        resultados.append('N')

for i in resultados:
    print(i)