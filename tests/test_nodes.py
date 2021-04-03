import unittest
from usecases.Nodos import Nodo

class NodeTest(unittest.TestCase):

  def testNodeInicial(self):
    nodoInicial = Nodo('Nodo Inicial', ['proximo'])
    self.assertEqual(len(nodoInicial.arrayNodo), 1, 'Nodo inicial não criado')

if __name__ == "__main__":
  unittest.main()

if __name__ == "__main__" and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))