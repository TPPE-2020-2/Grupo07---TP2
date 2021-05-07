
class FragmentsRefactor():
    arrayFragments = []
    def __init__(self, nome="", condicao_guarda=True, representedBy = ""):
        try:
            fragmento_opcional = {
                'nome': nome,
                'condicao_guarda': condicao_guarda,
                'representedBy': representedBy
            }
            isValidFragment = self.validateFragment(fragmento_opcional)
            if isValidFragment:
                self.addFragment(fragmento_opcional)

        except Exception as error:
            print('Fragmento Opcional', error)

    def addFragment(self, fragmento_opcional):
        self.arrayFragments.append(fragmento_opcional)

    def validateFragment(self, fragmento):
        if fragmento['condicao_guarda']:
            return True
        elif not fragmento['representedBy']:
            raise Exception('EmptyOptionalFragment')
        else:
            return False

# fragment = Fragments('teste', False, 'else')
# print(len(fragment.arrayFragments))