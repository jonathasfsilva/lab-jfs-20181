"""Quebrando a banca."""
saida = []
while True:
    try:
        entrada = input().split()
        tamanho, tirar = int(entrada[0]), int(entrada[1])
        saldo = str(input())
        saldo = [int(x) for x in saldo]
        inicio = 0
        fim = tamanho - tirar + 1
        resultado = []
        for x in range(tamanho - tirar, 0, -1):
            maior = max(saldo[inicio:fim])
            resultado.append(str(maior))
            inicio = saldo[inicio:].index(maior) + inicio + 1
            fim = tamanho - x + 2
        plote = ''
        saida.append(plote.join(resultado))
    except:
        pass
        for i in saida:
            print(i)
        break
