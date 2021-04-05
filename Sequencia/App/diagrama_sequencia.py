import xml.etree.cElementTree as ET


class DiagramaSequencia:
    def __init__(self, nome: str, condicao_guarda: bool):
        self.nome = nome
        self.condicao_guarda = condicao_guarda

    def CadastrarDiagramaSequencia(self):

        SequenceDiagram = ET.Element("SequenceDiagrams")
        Lifelines = ET.SubElement(SequenceDiagram, "Lifelines")

        ET.SubElement(Lifelines, "Lifeline", name='Lifeline 1')
        #ET.SubElement(SequenceDiagram, "SequenceDiagram", name='Lifeline 1', condicao_guarda=self.condicao_guarda)

        tree = ET.ElementTree(SequenceDiagram)
        tree.write("filename.xml")

diagrama1 = DiagramaSequencia("Teste", "condicao")
diagrama1.CadastrarDiagramaSequencia()



