
class ListaDeCompras:

    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def remover(self, item):
        self.itens.remove(item)

    def listar(self):
        return self.itens
