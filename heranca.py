u"""Herança."""


class Pessoa:
    """Classe Pessoa."""

    def __init__(self, nome, idade):
        """Construtor."""
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        """Return nome."""
        li = str(self.nome) + str(self.idade)
        return li


class Func(Pessoa):
    """docstring for Func."""

    def bla(self):
        """SS."""
        return self.name
