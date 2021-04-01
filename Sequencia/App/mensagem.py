import os.path

class Mensagem:
    def __init__(self, nome: str, prob: float, source: str, target: str):
        self.nome = nome
        self.prob = prob
        self.source = source
        self.target = target

        if not self.nome or not self.prob or not self.source or not self.target: 
            raise Exception('MessageFormatException')

    def CadastrarMensagem(self):

        # ARRUMAR A EXCEPTION PARA QUE VERIFIQUE SE ESTÁ FALTANDO PARÂMETRO
        # if not self.nome or not self.prob or not self.source or not self.target: 
        #     raise Exception('MessageFormatException')
        else:
            if os.path.exists("mensagem.txt"):
                mensagem_arq = open("mensagem.txt", 'r+')
                mensagem_lista = mensagem_arq.readlines()
                mensagem_lista.append(f'   < Message name = "{self.nome}" prob = {self.prob} source = {self.source} target = {self.target} / >' + '\n')
                mensagem_arq.writelines(mensagem_lista)
            else:
                mensagem_arq = open("mensagem.txt", 'w+')
                mensagem_lista = mensagem_arq.readlines()
                mensagem_lista.append(f'   < Message name = "{self.nome}" prob = {self.prob} source = {self.source} target = {self.target} / >' + '\n')
                mensagem_arq.writelines(mensagem_lista)
                return
        return

# mensagem1 = Mensagem(0.9,"teste2","teste3")
# mensagem1.CadastrarMensagem()