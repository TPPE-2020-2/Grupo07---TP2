from diagrama_sequencia import DiagramaSequencia

class Fragments:
    arrayFragments = []
    def __init__(self, nome: str, condicao_guarda: bool, representedBy = DiagramaSequencia(nome)):
        try:
            if not representedBy:
                raise Exception('EmptyOptionalFragment')
            
            fragmento_opcional = {
                self.nome = nome
                self.condicao_guarda = condicao_guarda
                self.representedBy = DiagramaSequencia(nome)
            }
            if condicao_guarda:
                self.arrayFragments.append(fragmento_opcional)
            else:
                pass

        except Exception as error:
            print('Fragmento Opcional', error)

    def addFragment(self, fragmento_opcional):
        self.arrayFragments.append(fragmento_opcional) 