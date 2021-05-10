class FragmentsArray():
    arrayFragments = []
    
    def addFragment(self, fragmento_opcional):
        fragmentoValido = fragmento_opcional.validateFragment()
        if fragmentoValido:
            self.arrayFragments.append(fragmento_opcional) 


class FragmentsPolimorfismo():
    def __init__(self, nome="", condicao_guarda=True, representedBy = ""):          
            fragmento_opcional = {
                'nome': nome,
                'condicao_guarda': condicao_guarda,
                'representedBy': representedBy
            }
        
            self.fragmento = fragmento_opcional

    def validateFragment(self):
        if self.fragmento['condicao_guarda']:
            return True
        elif not self.fragmento['representedBy']:
            raise Exception('EmptyOptionalFragment')
        else:
            return False
