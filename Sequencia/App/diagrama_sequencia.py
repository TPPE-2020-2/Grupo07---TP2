import xml.etree.cElementTree as ET

class DiagramaSequencia():
    def __init__(self, nome_diagrama = "", condicao_guarda="", lifelines=[], mensagens=[], fragmentos=[]):
        SequenceDiagram = ET.Element("SequenceDiagram", name=nome_diagrama)
        SequenceDiagramElements = ET.SubElement(SequenceDiagram, "SequenceDiagramElements")
        
        return Lifeline(self.lifelines)
        return Mensagem(self.mensagens)
        return Fragmentos(self.Fragmentos)
                   
        tree = ET.ElementTree(SequenceDiagram)
        tree.write("diagrama_sequencia.xml")

class Lifeline():
    def __init__(self, lifelines=[]):
        for lifeline in self.lifelines:
            ET.SubElement(SequenceDiagramElements, "Lifeline", name=lifeline)
class Mensagem():
    def __init__(self, mensagens=[]):
        for mensagem in self.mensagens:
            ET.SubElement(SequenceDiagramElements, "Message", name=mensagem['name'], prob=str(mensagem['prob']),source=mensagem['source'], target=mensagem['target'])      
class Fragmentos():
   def __init__(self, fragmentos=[]):
        for fragmento_opcional in self.fragmentos:
            ET.SubElement(SequenceDiagramElements, "Fragmento Opcional", name=fragmento_opcional['nome'], condicao_guarda=str(fragmento_opcional['condicao_guarda']),representedBy=fragmento_opcional['representedBy'])
           

# diagrama1 = DiagramaSequencia("Teste", "condicao")
# diagrama1.CadastrarDiagramaSequencia()



