"""Start."""

import roboColecionador

a = roboColecionador.Robo(0, 0, 0)

"""linha, coluna"""

ar = roboColecionador.Arena(2, 3, a)
print(a.posicao)
print(ar)
roboColecionador.Arena.anda(a)
print(a.posicao)
print(ar)
