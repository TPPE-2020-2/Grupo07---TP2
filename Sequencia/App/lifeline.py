import os.path

class Lifelines: 
    def __init__(self, nome: str):
        self.nome = nome

    def CriarLifelines(self):

        if os.path.exists("lifelines.txt"):
            lifelines_arq = open("lifelines.txt", 'r')
            lifelines_lista = lifelines_arq.readlines()
            lifelines_arq.close()

            lifelines_lista.insert(len(lifelines_lista)-1, f'   < Lifeline name="{self.nome}"/>' + '\n')
            
            lifelines_arq = open("lifelines.txt", 'w')
            lifelines_lista = "".join(lifelines_lista)
            lifelines_arq.write(lifelines_lista)
            lifelines_arq.close()
        else:
            lifelines_arq = open("lifelines.txt", 'w+')
            lifelines_lista = lifelines_arq.readlines()
            lifelines_lista.append("< Lifelines >" + '\n')
            lifelines_lista.append(f'   < Lifeline name="{self.nome}"/>' + '\n')
            lifelines_lista.append("</ Lifelines >" + '\n')
            lifelines_arq.writelines(lifelines_lista)
            return

# life1 = Lifelines("teste1")
# life2 = Lifelines("teste2")
# life2.CriarLifelines()