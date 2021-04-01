class Nodo:
    arrayNodo = []

    def __init__(self, nomeNodoInicial= "", nomeNodoDestino = []):
        try:
            if (len(nomeNodoDestino) > 1):
                raise Exception('ActivityDiagramRuleException')

            nodoInicial = {
                "nomeNodoInicial": nomeNodoInicial,
                "nomeNodoDestino": nomeNodoDestino[0]
            }
            self.arrayNodo.append(nodoInicial)
        except Exception as error:
            print('Nodo Inicial', error)

    def addNodo(self, nodo):
        self.arrayNodo.append(nodo) 

class NodoDecisao:
    def __init__(self, nomeNodoDecisao = "", nomeNodoOrigem = [], nomeNodoDestino = [], probabilidade = 0):
        try:
            if (len(nomeNodoOrigem) > 1):
                raise Exception('ActivityDiagramRuleException')
            
            nodo = {
                'nomeNodoDecisao': nomeNodoDecisao,
                'nomeNodoOrigem': nomeNodoOrigem,
                'nomeNodoDestino': nomeNodoDestino,
                'probabilidade': probabilidade
            }
            self.nodo = nodo
        except Exception as error:
            print('Nodo Decisao', error)


class NodoFusao:
    def __init__(self, nomeNodoFusao = "", nomeNodoOrigem = [], nomeNodoDestino = [], probabilidade = 0):
        try:
            if (len(nomeNodoDestino) > 1):
                raise Exception('ActivityDiagramRuleException')

            nodo = {
                'nomeNodoFusao': nomeNodoFusao,
                'nomeNodoOrigem': nomeNodoOrigem,
                'nomeNodoDestino': nomeNodoDestino,
                'probabilidade': probabilidade
            }
            self.nodo = nodo
        except Exception as error:
            print('Nodo Fusão', error)
        

class NodoFinal:
    def __init__(self, nomeNodoFinal= "", nomeNodoOrigem = [], nomeNodoDestino = ''):
        try:
            if (nomeNodoDestino != NULL):
                raise Exception('ActivityDiagramRuleException')
            
            nodoFinal = {
                "nomeNodoFinal": nomeNodoFinal,
                "nomeNodoOrigem": nomeNodoOrigem
            }
            self.nodo = nodoFinal
        except Exception as error:
            print('Nodo Fusão', error)

print('nodo inicial')
nodo = Nodo('inicial', ['segundo'])
# nodoDecisao = NodoDecisao('decisao', 'inicial', 'terceiro', 0)
print(nodo.arrayNodo)
# print('nodo decisao')
# print(nodoDecisao.nodo)
# nodo.addNodo(nodoDecisao.nodo)
# print('nodo atualizado')
# print(nodo.arrayNodo)
# nodoFusao = NodoFusao('fusao', 'sei la', 'quarto', 0)
# nodo.addNodo(nodoFusao.nodo)
# print('nodo atualizado')
# print(nodo.arrayNodo)
# nodoFinal = NodoFinal('final', 'quarto')
# nodo.addNodo(nodoFinal.nodo)
# print('nodo atualizado')
# print(nodo.arrayNodo)

