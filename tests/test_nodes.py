# -*- coding: utf-8 -*-
import unittest
import os

from usecases.Nodos import Nodo, NodoDecisao, NodoFusao, NodoFinal
class testeNodo(unittest.TestCase):

  def testNodeInicial(self):
    nodoInicial = Nodo('Nodo Inicial', ['proximo'])
    self.assertEqual(len(nodoInicial.arrayNodo), len(nodoInicial.arrayNodo), 'Nodo inicial não criado')
  
  def testNodeDecisao(self):
    nodoDecisao = NodoDecisao('Nodo Decisao', ['Nodo Inicial'] ,['Nodo Fusao'])
    self.assertEqual(nodoDecisao.nodo['nomeNodo'], 'Nodo Decisao', 'Nodo decisao não criado')
    self.assertEqual(nodoDecisao.nodo['nomeNodoOrigem'], ['Nodo Inicial'], 'Nodo decisao não criado')

  def testNodeFusao(self):
    nodoFusao = NodoFusao('Nodo Fusao', ['Nodo Decisao'] ,['Nodo Final'])
    self.assertEqual(nodoFusao.nodo['nomeNodo'], 'Nodo Fusao', 'Nodo fusao não criado')
    self.assertEqual(nodoFusao.nodo['nomeNodoOrigem'], ['Nodo Decisao'], 'Nodo fusao não criado')

  def testNodeFinal(self):
    nodoFinal = NodoFinal('Nodo Final', ['Nodo Fusao'])
    self.assertEqual(nodoFinal.nodo['nomeNodo'], 'Nodo Final', 'Nodo final não criado')
    self.assertEqual(nodoFinal.nodo['nomeNodoOrigem'], ['Nodo Fusao'], 'Nodo final não criado')

"""if __name__ == "__main__":
  unittest.main()"""

if __name__ == "__main__" and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))