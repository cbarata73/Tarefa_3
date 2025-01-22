import time
import unittest
from chat_bot import obter_resposta, chat

class TestChatBot(unittest.TestCase):
    def test_resposta_valida(self):
        self.assertEqual(obter_resposta("Capital de Portugal?"), "Lisboa")

    def test_resposta_invalida(self):
        self.assertEqual(obter_resposta("Pergunta estranha?"), "Desculpa, não entendi a questão! Pergunta estranha?")

    def test_resposta_nula(self):
        self.assertEqual(obter_resposta(''), "Desculpa, não entendi a questão! ")

    def test_resposta_varios_parametros(self):
        self.assertEqual(obter_resposta("historia de portugal."), "Portugal tem uma rica história...")

    def test_performance(self):
        start_time = time.time()
        obter_resposta("Pergunta complexa" * 1000)  # Simula uma entrada complexa
        self.assertTrue(time.time() - start_time < 1)  # Deve ser executado em menos de 1 segundo

    def test_obter_resposta(self):
        # Teste de exemplo para a função obter_resposta
        resposta = obter_resposta("Olá")
        self.assertIsInstance(resposta, str)  # Verifica se a resposta é uma string
        self.assertEqual(obter_resposta("Olá"), 'Olá tudo bem!')
        self.assertEqual(obter_resposta("boa tarde"), 'Olá tudo bem!')

    def test_chat(self):
        # Teste de exemplo para a função chat
        # Simular a interação do chat
        self.assertIsNone(chat())  # Verifica se a função não retorna nada

if __name__ == '__main__':
    unittest.main()
# python -m unittest -v testar_chat_bot.py
