import unittest
from mensagens import Mensagem

class MensagensTest(unittest.TestCase):
    def setUp(self):
        self.mensagem = Mensagem()

    #falsificacao    
    def test_get_name_mensagem_fals(self):
        self.assertEqual(self.mensagem.get_name_fals(), 'Mensagem 1')

    def test_set_name_mensagem(self):
        self.mensagem.set_name(self.mensagem.name)
        self.assertEqual(self.mensagem.get_name(), self.mensagem.name)

    def test_set_prob_mensagem(self):
        self.mensagem.set_prob(self.mensagem.prob)
        self.assertEqual(self.mensagem.get_prob(), self.mensagem.prob)

    def test_set_source_mensagem(self):
        self.mensagem.set_source(self.mensagem.source)
        self.assertEqual(self.mensagem.get_source(), self.mensagem.source)

    def test_set_target_mensagem(self):
        self.mensagem.set_target(self.mensagem.target)
        self.assertEqual(self.mensagem.get_target(), self.mensagem.target)


if __name__ == "__main__":
  unittest.main()