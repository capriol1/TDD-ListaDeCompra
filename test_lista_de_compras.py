# test_lista_de_compras.py
import unittest
from lista_de_compras import ListaDeCompras

class TestListaDeCompras(unittest.TestCase):

    def setUp(self):
        self.lista = ListaDeCompras()

    def test_adicionar_item(self):
        self.lista.adicionar("Maçã")
        self.assertIn("Maçã", self.lista.listar())

    def test_remover_item(self):
        self.lista.adicionar("Maçã")
        self.lista.remover("Maçã")
        self.assertNotIn("Maçã", self.lista.listar())

    def test_listar_itens(self):
        itens = ["Maçã", "Banana", "Cenoura"]
        for item in itens:
            self.lista.adicionar(item)
        for item in itens:
            self.assertIn(item, self.lista.listar())


if __name__ == "__main__":
    unittest.main()
