from App.diagrama_sequencia import DiagramaSequencia
from App.mensagens import Mensagem, MensagemAssincrona, MensagemSincrona, MensagemResposta
from App.lifeline import Lifeline
from App.fragments import Fragments

if __name__ == '__main__':
    lifeline1 = Lifeline('Lifeline1')
    lifeline2 = Lifeline('Lifeline2')
    mensagem_sincrona = Mensagem('Mensagem Sincrona', 0.5, 'Source', 'Terget')
    mensagem_assincrona = Mensagem('Mensagem Assincrona', 0.8, 'Lifeline1', 'Lifeline2')
    fragment = Fragments('Fragmento Opcional', True, 'Nome do diagrama')

    diagrama = DiagramaSequencia('Nome do diagrama', 'condicao', lifeline1.arrayLifeline, mensagem_sincrona.arrayMensagem, fragment.arrayFragments)