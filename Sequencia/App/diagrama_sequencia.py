import xml.etree.cElementTree as ET


class DiagramaSequencia():
    def __init__(self, nome_diagrama = "", condicao_guarda="", lifelines=[], mensagens=[], fragmentos=[]):
            self.nome_diagrama = nome_diagrama
            self.condicao_guarda = condicao_guarda
            self.lifelines = lifelines
            self.mensagens = mensagens
            self.fragmentos = fragmentos

class CriarDiagramaSequencia(DiagramaSequencia):
        def __init__(self, nome_diagrama, condicao_guarda, lifelines, mensagens, fragmentos):
                
                SequenceDiagram = ET.Element("SequenceDiagram", name=nome_diagrama)
                SequenceDiagramElements = ET.SubElement(SequenceDiagram, "SequenceDiagramElements")

                def criar_lifelines():
                        for lifeline in lifelines:
                                ET.SubElement(SequenceDiagramElements, "Lifeline", name=lifeline)
                                tree = ET.ElementTree(SequenceDiagram)
                                tree.write("diagrama_sequencia.xml")

                def criar_mensagens():
                        for mensagem in mensagens:
                                ET.SubElement(SequenceDiagramElements, "Message", name=mensagem['name'], prob=str(mensagem['prob']),source=mensagem['source'], target=mensagem['target'])
                                tree = ET.ElementTree(SequenceDiagram)
                                tree.write("diagrama_sequencia.xml")
                
                def criar_fragmentos():
                        for fragmento_opcional in fragmentos:
                                ET.SubElement(SequenceDiagramElements, "Fragmento Opcional", name=fragmento_opcional['nome'], condicao_guarda=str(fragmento_opcional['condicao_guarda']),representedBy=fragmento_opcional['representedBy'])
                                tree = ET.ElementTree(SequenceDiagram)
                                tree.write("diagrama_sequencia.xml")

                adicionar_lifelines = criar_lifelines()
                adicionar_mensagens = criar_mensagens()
                adicionar_fragmentos = criar_fragmentos()

# diagrama1 = DiagramaSequencia("Teste", "condicao")
# diagrama1.CadastrarDiagramaSequencia()



