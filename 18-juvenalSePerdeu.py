"""Juvenal se perdeu."""

from arvore import No
from arvore import Arvore

"""
cont = 1
while True:
    n = input()
    arv = Arvore()
    if n == '':
        break
    print('Caso %d:'%(cont))
    cont += 1
    for i in range(int(n)):
        entrada = input().split()
        if len(entrada) == 1:
            cmd = entrada[0]
            if cmd == 'PRE':
                plot = arv.preOrdem(arv.getRaiz())
                if plot == '':
                    print(0)
                else:
                    print(plot)
            elif cmd == 'IN':
                arv.emOrdem(arv.getRaiz())
                print()
            elif cmd == 'POST':
                arv.posOrdem(arv.getRaiz())
                print()
        else:
            if entrada[0] == 'A':
                no = No(entrada[1], entrada[1])
                arv.insere(no)
            elif entrada[0] == 'B':
                y = arv.busca(entrada[1])
                x = arv.remove(arv.busca(entrada[1]))
                print(y)
            elif entrada[0] == 'C':
                plot = arv.sucessor(arv.busca(entrada[1]))
                if plot is None:
                    print('0')
                else:
                    print(plot)"""

resultados = []
comandos = []
caso = 0

while True:
    entrada = input()
    if entrada == '':
        break
    else:
        comandos.append(entrada)

for i in range(len(comandos)):
    entrada = comandos[i].split()
    if entrada[0].isdigit():
        caso += 1
        qtd = int(entrada[0])
        print('Caso {}: '.format(caso))
        arvore = Arvore()

        for j in comandos[i+1:(i+qtd)+1]:
            if j[0] == 'A':
                arvore.insere(No(int(j[2:]), int(j[2:])))
            elif j[0] == 'B':
                arvore.remove(arvore.busca(int(j[2:])))
            elif j[0] == 'C':
                no = arvore.busca(int(j[2:]))
                if arvore.estaVazia():
                    print(0)
                elif arvore.minimo(no) == no:
                    print(0)
                else:
                    print(arvore.antecessor(no))
            elif j == 'PRE':
                if arvore.estaVazia():
                    print(0)
                else:
                    arvore.preOrdem(arvore.getRaiz())
                    print()
            elif j == 'IN':
                if arvore.estaVazia():
                    print(0)
                else:
                    arvore.emOrdem(arvore.getRaiz())
                    print()
            elif j == 'POST':
                if arvore.estaVazia():
                    print(0)
                else:
                    arvore.posOrdem(arvore.getRaiz())
                    print()
