"""Linhas cruzadas"""

n = int(input())
pregos = input().split(' ')
pregos = [int(i) for i in pregos]
cruzamentos = 0

for i in range(len(pregos)):
    for j in range(i+1, len(pregos)):
        if pregos[j] < pregos[i]:
            cruzamentos += 1

print(cruzamentos)