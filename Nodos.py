class Nodo:
    arrayNodo = []

    def __init__(self, nomeNodoInicial= "", nomeNodoDestino = ""):
        self._nomeNodoInicial = nomeNodoInicial  
        self._nomeNodoDestino = nomeNodoDestino

    def addNodo(self, nodo):
        arrayNodo.append(nodo) 

class NodoDecisao(self):
    def __init__(self, nomeNodoDecisao = "", nomeNodoOrigem = "", nomeNodoDestino = "", probabilidade = 0):
        self._nomeNodoDecisao = nomeNodoDecisao
        self._nomeNodoOrigem = nomeNodoOrigem
        self._nomeNodoDestino = nomeNodoDestino
        self._probabilidade = probabilidade

class NodoFusao(self):
    def __init__(self, nomeNodoFusao = "", nomeNodoOrigem = "", nomeNodoDestino = "", probabilidade = 0):
        self._nomeNodoFusao = nomeNodoFusao
        self._nomeNodoOrigem = nomeNodoOrigem
        self._nomeNodoDestino = nomeNodoDestino
        self._probabilidade = probabilidade

class NodoFinal(self):
    def __init__(self, nomeNodoInicial= "", nomeNodoOrigem = ""):
        self._nomeNodoInicial = nomeNodoInicial  
        self._nomeNodoOrigem = nomeNodoOrigem
