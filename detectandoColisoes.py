"""Exec1LAb."""
linha = input().split()

ax0, ay0, ax1, ay1 = linha

linha2 = input().split()

bx0, by0, bx1, by1 = linha2

if int(ax0) <= int(bx0) <= int(ax1):
    print(1)
elif int(ay0) <= int(by0) <= int(ay1):
    print(1)
else:
    print(0)
