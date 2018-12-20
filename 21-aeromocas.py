u"""Aeromoças."""
from math import inf


class Vertice():
    """Class vertice."""

    def __init__(self, id):
        u"""
        Classe Vertice.

        atributos
            id
            distancia
            vizinhos
            arestas

        métodos
            adicionaAresta
            adicionaVizinho
        """
        self.id = str(id)
        self.distancia = 0
        self.vizinhos = []
        self.arestas = {}

    def __lt__(self, other):
        u"""Metodo mágico para o operador de '<'."""
        return (self.distancia < other.distancia)

    def __repr__(self):
        """Retorna o id do vertice."""
        return self.id

    def adicionaVizinho(self, Vertice):
        """Adiciona um ponteiro para um Vertice na lista do vizinho."""
        self.vizinhos.append(Vertice)

    def adicionaAresta(self, Vertice, distancia):
        """Adiciona a distancia da arestas."""
        try:
            if distancia < self.arestas[Vertice.id]:
                self.arestas[Vertice.id] = distancia
        except:
            self.arestas[Vertice.id] = distancia


def minimo(lista):
    """Retorna o minimo de um lista."""
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor


def dijkstra(grafo, origem, destino):
    """Algoritmo de Dijkstra."""
    Q = []
    for v in grafo:
        v.distancia = inf
        Q.append(v)
    origem.distancia = 0
    while Q:
        v = minimo(Q)
        Q.remove(v)
        for u in v.vizinhos:
            novo = v.distancia + v.arestas[u.id]
            if novo < u.distancia:
                u.distancia = novo
    return destino.distancia


N, M = input().split()
N, M = int(N), int(M)
rotas = [input().split() for i in range(M)]
cidades = [Vertice(n) for n in range(N)]

for r in rotas:
    cidades[int(r[0])].adicionaVizinho(cidades[int(r[1])])
    cidades[int(r[1])].adicionaVizinho(cidades[int(r[0])])
    cidades[int(r[0])].adicionaAresta(cidades[int(r[1])], int(r[2]))
    cidades[int(r[1])].adicionaAresta(cidades[int(r[0])], int(r[2]))

maximos = []
for i in range(len(cidades)):
    maximo = 0
    for j in range(len(cidades)):
        atual = dijkstra(cidades, cidades[i], cidades[j])
        if atual > maximo:
            maximo = atual
    maximos.append(maximo)

print(minimo(maximos))
