"""Decifra."""

cifra = input()
mensagem = input()
dicionario = {}

cifra = [x for x in cifra]

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for x in range(len(cifra)):
    dicionario[cifra[x]] = alfabeto[x]

mensagem = [x for x in mensagem]

traducao = [dicionario[letra] for letra in mensagem]

for l in traducao:
    print(l, end='')
print()
