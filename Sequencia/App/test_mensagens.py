import unittest
from mensagens import Mensagem, MensagemSincrona, MensagemAssincrona, MensagemResposta

class MensagensTest(unittest.TestCase):
    def test_mensagem_sincrona(self):
        mensagem_sincrona = MensagemSincrona('Sincrona1', 0.0, 'Source', 'Target')
        self.assertEqual(mensagem_sincrona.mensagem['name'], 'Sincrona1')
        self.assertEqual(mensagem_sincrona.mensagem['prob'], 0.0)
        self.assertEqual(mensagem_sincrona.mensagem['source'], 'Source')
        self.assertEqual(mensagem_sincrona.mensagem['target'], 'Target')

    def test_mensagem_assincrona(self):
        mensagem_assincrona = MensagemAssincrona('Assincrona1', 0.1, 'Source2', 'Target2')
        self.assertEqual(mensagem_assincrona.mensagem['name'], 'Assincrona1')
        self.assertEqual(mensagem_assincrona.mensagem['prob'], 0.1)
        self.assertEqual(mensagem_assincrona.mensagem['source'], 'Source2')
        self.assertEqual(mensagem_assincrona.mensagem['target'], 'Target2')

    def test_resposta(self):
        resposta = MensagemResposta('Resposta', 0.6, 'Source3', 'Target3')
        self.assertEqual(resposta.mensagem['name'], 'Resposta')
        self.assertEqual(resposta.mensagem['prob'], 0.6)
        self.assertEqual(resposta.mensagem['source'], 'Source3')
        self.assertEqual(resposta.mensagem['target'], 'Target3')
#     def setUp(self):
#         self.mensagem = Mensagem()

#     #falsificacao    
#     def test_get_name_mensagem_fals(self):
#         self.assertEqual(self.mensagem.get_name_fals(), 'Mensagem 1')

#     def test_set_name_mensagem(self):
#         self.mensagem.set_name(self.mensagem.name)
#         self.assertEqual(self.mensagem.get_name(), self.mensagem.name)

#     def test_set_prob_mensagem(self):
#         self.mensagem.set_prob(self.mensagem.prob)
#         self.assertEqual(self.mensagem.get_prob(), self.mensagem.prob)

#     def test_set_source_mensagem(self):
#         self.mensagem.set_source(self.mensagem.source)
#         self.assertEqual(self.mensagem.get_source(), self.mensagem.source)

#     def test_set_target_mensagem(self):
#         self.mensagem.set_target(self.mensagem.target)
#         self.assertEqual(self.mensagem.get_target(), self.mensagem.target)


# if __name__ == "__main__":
#   unittest.main()