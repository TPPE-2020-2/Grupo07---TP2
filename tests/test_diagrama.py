import unittest
from usecases.Atividades import Atividade
from usecases.Nodos import Nodo, NodoDecisao, NodoFusao, NodoFinal

class testeAtividade(unittest.TestCase):

  def testCriacaoDiagrama(self):
    nodoInicial = Nodo('Nodo Inicial', ['proximo'])
    nodoDecisao = NodoDecisao('Nodo Decisao', ['Nodo Inicial'] ,['Nodo Fusao'])
    nodoFusao = NodoFusao('Nodo Fusao', ['Nodo Decisao'] ,['Nodo Final'])
    nodoFinal = NodoFinal('Nodo Final', ['Nodo Fusao'])
    nodoInicial.addNodo(nodoDecisao)
    nodoInicial.addNodo(nodoFusao)
    nodoInicial.addNodo(nodoFinal)
    self.assertEqual(len(nodoInicial.arrayNodo), 4, 'Nodos não criados')
    atividade = Atividade('Diagrama de Atividades', 'Atividade de Monitoramento', nodoInicial.arrayNodo)
    self.assertEqual(nodoInicial['nomeDiagrama'], 'Diagrama de Atividades', 'Nome do diagrama não criado')
    self.assertEqual(nodoInicial['nomeAtividade'], 'Atividade de Monitoramento', 'Nome da atividade não criado')
    self.assertEqual(len(nodoInicial['arrayAtividades']), 4, 'Atividades não foram criadas')
    self.assertEqual(len(nodoInicial['arrayTransicoes']), 4, 'Transicoes não foram criadas')

if __name__ == "__main__":
  unittest.main()

if __name__ == "__main__" and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))