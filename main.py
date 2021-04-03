from tests.test_nodes import testeNodo
from tests.test_atividade import testeAtividade
from usecases.Nodos import Nodo, NodoDecisao, NodoFusao, NodoFinal
from usecases.Atividades import Atividade
from usecases.Diagramas import Diagrama
import unittest

if __name__ == "__main__":
  unittest.main()
  newNode = Nodo('Inicial', ['Decisao'])
  nodoDecisao = NodoDecisao('Decisao', ['Inicial'], ['Fusao', 'Decisao2'])
  nodoDecisao2 = NodoDecisao('Decisao2', ['Decisao'], ['Final'])
  nodoFusao = NodoFusao('Fusao', ['Decisao'], ['Final'])
  nodoFinal = NodoFinal('Final', ['Decisao2', 'Fusao'])
  newNode.addNodo(nodoDecisao.nodo)
  newNode.addNodo(nodoDecisao2.nodo)
  newNode.addNodo(nodoFusao.nodo)
  newNode.addNodo(nodoFinal.nodo)
  atividade = Atividade('diagrama', 'atividade teste', newNode.arrayNodo)
  diagrama = Diagrama(atividade.arrayAtividades, atividade.arrayTransicoes, atividade.nomeDiagrama, atividade.nomeAtividade)
  