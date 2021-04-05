import xml.etree.cElementTree as ET


class DiagramaSequencia():
    def __init__(self, nome_diagrama = "", condicao_guarda="", lifelines=[], mensagens=[], fragmentos=[]):
        SequenceDiagram = ET.Element("SequenceDiagram", name=nome_diagrama)
        SequenceDiagramElements = ET.SubElement(SequenceDiagram, "SequenceDiagramElements")
        for lifeline in lifelines:
                ET.SubElement(SequenceDiagramElements, "Lifeline", name=lifeline)
        for mensagem in mensagens:
                ET.SubElement(SequenceDiagramElements, "Message", name=mensagem['name'], prob=str(mensagem['prob']),source=mensagem['source'], target=mensagem['target'])
        for fragmento_opcional in fragmentos:
                ET.SubElement(SequenceDiagramElements, "Fragmento Opcional", name=fragmento_opcional['nome'], condicao_guarda=str(fragmento_opcional['condicao_guarda']),representedBy=fragmento_opcional['representedBy'])


        


        tree = ET.ElementTree(SequenceDiagram)
        tree.write("diagrama_sequencia.xml")

# diagrama1 = DiagramaSequencia("Teste", "condicao")
# diagrama1.CadastrarDiagramaSequencia()



