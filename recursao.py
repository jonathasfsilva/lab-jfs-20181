def substring(nome, i, j):
    tamanho = len(nome)
    if j <= tamanho:
        j += 1
        print(nome[i:j])
        return substring(nome, i ,j)
    else:
        print()
        return False

def substring2(nome, c = 1):
    print(nome[:c+1])
    if c < len(nome):
        substring2(nome, c+1)
    elif len(nome) > 1:
        substring2(nome[1:])

nome = input()
substring2(nome)

"""
for i in range(len(nome)):
    j = i + 1
    substring(nome, i, j)"""
