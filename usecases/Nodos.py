# -*- coding: utf-8 -*-
class Nodo:
    arrayNodo = []

    def __init__(self, nomeNodo= "", nomeNodoDestino = []):
        try:
            if (len(nomeNodoDestino) > 1):
                raise Exception('ActivityDiagramRuleException')

            nodoInicial = {
                "nomeNodo": nomeNodo,
                "nomeNodoDestino": nomeNodoDestino[0],
                'tipo': 'inicial'
            }
            self.nodoInicial = nodoInicial
            self.arrayNodo.append(nodoInicial)
        except Exception as error:
            print('Nodo Inicial', error)

    def addNodo(self, nodo):
        self.arrayNodo.append(nodo) 

class NodoDecisao:
    def __init__(self, nomeNodo = "", nomeNodoOrigem = [], nomeNodoDestino = []):
        try:
            if (len(nomeNodoOrigem) > 1):
                raise Exception('ActivityDiagramRuleException')
            
            nodo = {
                'nomeNodo': nomeNodo,
                'nomeNodoOrigem': nomeNodoOrigem,
                'nomeNodoDestino': nomeNodoDestino,
                'tipo': 'decisao'
            }
            self.nodo = nodo
        except Exception as error:
            print('Nodo Decisao', error)


class NodoFusao:
    def __init__(self, nomeNodo = "", nomeNodoOrigem = [], nomeNodoDestino = []):
        try:
            if (len(nomeNodoDestino) > 1):
                raise Exception('ActivityDiagramRuleException')

            nodo = {
                'nomeNodo': nomeNodo,
                'nomeNodoOrigem': nomeNodoOrigem,
                'nomeNodoDestino': nomeNodoDestino,
                'tipo': 'fusao'
            }
            self.nodo = nodo
        except Exception as error:
            print('Nodo Fusão', error)
        

class NodoFinal:
    def __init__(self, nomeNodo= "", nomeNodoOrigem = [], nomeNodoDestino = None):
        try:
            if (nomeNodoDestino != None):
                raise Exception('ActivityDiagramRuleException')
            
            nodo = {
                "nomeNodo": nomeNodo,
                "nomeNodoOrigem": nomeNodoOrigem,
                'tipo': 'final'
            }
            self.nodo = nodo
        except Exception as error:
            print('Nodo Final', error)

if __name__ == "__main__" and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))