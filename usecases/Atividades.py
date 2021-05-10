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
      'nomeNodo': ['nomeNodo'],
      'tipo': ['tipo']
    }

  def associacoes(self, nomeOrigem = "", nomeDestino = "", quantidadeDestinos = 1):
    return {
      'nome': str(nomeOrigem) + '-' + str(nomeDestino),
      'prob': 1 / quantidadeDestinos
    }
  
  def criarAssociacoes(self, nodos):
    for nodo in nodos:
      print(nodo)
      if(['tipo'] == 'final'):
        continue
      elif(['tipo'] != 'inicial' and len(['nomeNodoDestino']) > 1):
        for destino in ['nomeNodoDestino']:
            self.arrayTransicoes.append(self.associacoes(['nomeNodo'], destino, len(['nomeNodoDestino'])))
      elif(len(['nomeNodoDestino']) == 1) :
        self.arrayTransicoes.append(self.associacoes(['nomeNodo'], ['nomeNodoDestino'][0]))
      else:
        self.arrayTransicoes.append(self.associacoes(['nomeNodo'], ['nomeNodoDestino']))
    print(self.arrayTransicoes)