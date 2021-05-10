from App.diagrama_sequencia import CriarDiagramaSequencia
from App.mensagens import AdicionarMensagem, MensagemAssincrona, MensagemSincrona, MensagemResposta
from App.lifeline import Lifeline
from App.fragments import Fragments

if __name__ == '__main__':
    lifeline1 = Lifeline('Lifeline1')
    lifeline2 = Lifeline('Lifeline2')
    mensagem_sincrona = AdicionarMensagem('Mensagem Sincrona', 0.32, 'Source', 'Terget')
    mensagem_assincrona = AdicionarMensagem('Mensagem Assincrona', 0.23, 'Lifeline1', 'Lifeline2')
    resposta = AdicionarMensagem('Resposta', 0.57, 'Lifeline 2', 'Lifeline 1')
    fragment = Fragments('Fragmento Opcional', True, 'Nome do diagrama')

    diagrama = CriarDiagramaSequencia('Nome do diagrama', 'condicao', lifeline1.arrayLifeline, mensagem_sincrona.arrayMensagem, fragment.arrayFragments)