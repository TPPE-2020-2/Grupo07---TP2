import os.path

class Lifeline: 
    arrayLifeline = []
    def __init__(self, nomeLifeline =""):
        self.nomeLifeline = nomeLifeline
        
        self.arrayLifeline.append(nomeLifeline)
        

    def addLifeline(self, nomeLifeline):
        self.arrayLifeline.append(nomeLifeline) 
        

    #falsificacao
    def get_name_fals(self):
      return 'Lifeline fals'

    # def get_name(self):
    #     return self.name
    
    # def set_name(self, name):
    #     self.name = name

    

#     def CriarLifelines(self):

#         if os.path.exists("lifelines.txt"):
#             lifelines_arq = open("lifelines.txt", 'r')
#             lifelines_lista = lifelines_arq.readlines()
#             lifelines_arq.close()

#             lifelines_lista.insert(len(lifelines_lista)-1, f'   < Lifeline name="{self.name}"/>' + '\n')
            
#             lifelines_arq = open("lifelines.txt", 'w')
#             lifelines_lista = "".join(lifelines_lista)
#             lifelines_arq.write(lifelines_lista)
#             lifelines_arq.close()
#         else:
#             lifelines_arq = open("lifelines.txt", 'w+')
#             lifelines_lista = lifelines_arq.readlines()
#             lifelines_lista.append("< Lifelines >" + '\n')
#             lifelines_lista.append(f'   < Lifeline name="{self.name}"/>' + '\n')
#             lifelines_lista.append("</ Lifelines >" + '\n')
#             lifelines_arq.writelines(lifelines_lista)
#             return

# life1 = Lifeline("teste1")
# life2 = Lifeline("teste2")
# life2.CriarLifelines()
# life1.CriarLifelines()