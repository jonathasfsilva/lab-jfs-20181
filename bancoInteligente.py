"""Banco Inteligente."""

def contaFormas(valor, cedulas, cont):
    if valor == 0:
        cont += 1
    elif valor < 0:
        cont += 0
    else:
        if valor > cedulas[0]:
            contaFormas(valor-cedulas[0], cedulas[0]-1, cont)
        if valor > cedulas[1]:
            contaFormas(valor-cedulas[1], cedulas[1]-1, cont)
        if valor > cedulas[2]:
            contaFormas(valor-cedulas[2], cedulas[2]-1, cont)
        if valor > cedulas[3]:
            contaFormas(valor-cedulas[3], cedulas[3]-1, cont)
        if valor > cedulas[4]:
            contaFormas(valor-cedulas[4], cedulas[4]-1, cont)
        if valor > cedulas[5]:
            contaFormas(valor-cedulas[5], cedulas[5]-1, cont)


valor = int(input())
c2, c5, c10, c20, c50, c100 = input().split()

cedulas = [int(c2), int(c5), int(c10), int(20), int(50), int(100)]

formas = 0

print(contaFormas(valor, cedulas, formas))