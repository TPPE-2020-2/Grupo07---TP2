import os.path
import sys

class Mensagem:
    def __init__(self, name: str, prob: float, source: str, target: str):
        self.name = name
        self.prob = prob
        self.source = source
        self.target = target

         

    def CadastrarMensagem(self):

        # ARRUMAR A EXCEPTION PARA QUE VERIFIQUE SE ESTÁ FALTANDO PARÂMETRO
        # if not self.nome or not self.prob or not self.source or not self.target: 
        #     raise Exception('MessageFormatException')
        #else:
        if os.path.exists("msg.txt"):
            msg_arq = open("msg.txt", 'r')
            msg_lista = msg_arq.readlines()
            msg_arq.close()

            try:
                msg_lista.insert(len(msg_lista)-1, "< Message name = " + str(self.name) + " " + "prob = " + str(self.prob) + "source = " + str(self.source) + " target = " + str(self.target) + "/>" + '\n')

                if not self.name:
                    raise Exception('MessageFormatException')
            
            except:
                sys.exit('MessageFormatException') 

            msg_arq = open("msg.txt", 'w')
            msg_lista = "".join(msg_lista)
            msg_arq.write(msg_lista)
            msg_arq.close()
            

        else:
            msg_arq = open("msg.txt", 'w+')
            msg_lista.append("< Message >" + '\n')
            msg_lista.append(+" < Message  name = " + " " + str(self.name) + " "+" prob = " +" "+ str(self.prob) +" " + "source = " + " " + str(self.source) + " " + "target = " + " " + str(self.target) +  "/>" + '\n')
            msg_lista.append("</ Message >" + '\n')
            msg_arq.writelines(msg_lista)

        #try:
        #    if not self.name :
        #        raise Exception('MessageFormatException')                   
                    
            
        #except:
        #    sys.exit(1)    

                     
            
        return
                

#mensagem1 = Mensagem(None,0.9,"teste2","teste3")
#mensagem1.CadastrarMensagem()
mensagem2 = Mensagem("Sincrona", 0.8, "Lifeline1", "Lifeline2")
mensagem2.CadastrarMensagem()