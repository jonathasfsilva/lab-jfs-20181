u"""PeçaPerdida."""

n = int(input())
entrada = input().split()
lista = [str(x) for x in range(1, n+1)]
for i in lista:
    if i not in entrada:
        print(i)
        break
