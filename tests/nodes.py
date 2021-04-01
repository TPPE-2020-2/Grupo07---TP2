import unittest
import Nodos

class NodeTest(unittest.TestCase):

  def testNodeInicial(self):
    nodoInicial = Nodo('Nodo Inicial', 'proximo')
    self.assertEqual(nodoInicial.arrayNodo[0], 'Nodo Inicial', 'deu ruim')

if __name__ == "__main__":
  unittest.main()
  