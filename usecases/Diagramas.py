import xml.etree.cElementTree as ET

class Diagrama():
    def __init__(self, atividades = [], transicoes = [], nomeDiagrama = '', nomeAtividade = ''):
      DiagramaAtividade = ET.Element('ActivityDiagram', name=nomeDiagrama)
      ActivityDiagramElements = ET.SubElement(DiagramaAtividade, 'ActivityDiagramElements')
      for atividade in atividades:
        if(atividade['tipo'] == 'inicial'):
          ET.SubElement(ActivityDiagramElements, 'StartNode', name=atividade['nomeNodo'])
          ET.SubElement(ActivityDiagramElements, 'Activity', name=nomeAtividade)
        elif(atividade['tipo'] == 'decisao'):
          ET.SubElement(ActivityDiagramElements, 'DecisionNode', name=atividade['nomeNodo'])
        elif(atividade['tipo'] == 'fusao'):
          ET.SubElement(ActivityDiagramElements, 'MergeNode', name=atividade['nomeNodo'])
        elif(atividade['tipo'] == 'final'):
          ET.SubElement(ActivityDiagramElements, 'FinalNode', name=atividade['nomeNodo'])
      ActivityDiagramTransitions = ET.SubElement(DiagramaAtividade, 'ActivityDiagramTransitions')
      for transicao in transicoes:
        ET.SubElement(ActivityDiagramTransitions, 'Transition', name=transicao['nome'], prob=str(transicao['prob']))

      tree = ET.ElementTree(DiagramaAtividade)
      tree.write('DiagramaAtividades.xml')
