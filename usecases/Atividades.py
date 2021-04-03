class Atividade():
  arrayTransicoes = []
  arrayAtividades = []

  def __init__(self, nomeDiagrama = "", nomeAtividade = "", nodos = []):
    self.nodos = nodos
    self.nomeDiagrama = nomeDiagrama
    self.nomeAtividade = nomeAtividade
    self.criarAssociacoes(nodos)
    self.arrayAtividades = map(self.mapAtividades, nodos)

  def mapAtividades(self, nodo = ''):
    return {
      'nomeNodo': nodo['nomeNodo'],
      'tipo': nodo['tipo']
    }

  def associacoes(self, nomeOrigem = "", nomeDestino = "", quantidadeDestinos = 1):
    return {
      'nome': nomeOrigem + '-' + nomeDestino,
      'prob': 1 / quantidadeDestinos
    }
  
  def criarAssociacoes(self, nodos):
    for nodo in nodos:
      print(nodo)
      if(nodo['tipo'] == 'final'):
        continue
      elif(nodo['tipo'] != 'inicial' and len(nodo['nomeNodoDestino']) > 1):
        for destino in nodo['nomeNodoDestino']:
            self.arrayTransicoes.append(self.associacoes(nodo['nomeNodo'], destino, len(nodo['nomeNodoDestino'])))
      elif(len(nodo['nomeNodoDestino']) == 1) :
        self.arrayTransicoes.append(self.associacoes(nodo['nomeNodo'], nodo['nomeNodoDestino'][0]))
      else:
        self.arrayTransicoes.append(self.associacoes(nodo['nomeNodo'], nodo['nomeNodoDestino']))
    print(self.arrayTransicoes)