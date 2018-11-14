"""Expressoes."""

from lista import List
from lista import Node


class Pilha(List):
    """Classe pilha"""
    def push(self, dado):
        self.insertAtBegin(dado)

    def pop(self):
        return self.removeFromBegin()




n = int(input())


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

resultados = []

for i in range(n):
    expressao = input()
    if verifica(expressao):
        resultados.append('S')
    else:
        resultados.append('N')

for i in resultados:
    print(i)