import unittest
import math
from calculadora import calculadora_v2

class TestCalculadoraV2(unittest.TestCase):
    def test_adicao(self):
        """Testa a operação de adição"""
        self.assertEqual(calculadora_v2(5, 3, "+"), 8)
        self.assertEqual(calculadora_v2(-1, 1, "+"), 0)
        self.assertEqual(calculadora_v2(0, 0, "+"), 0)
        self.assertEqual(calculadora_v2(1.5, 2.5, "+"), 4.0)

    def test_subtracao(self):
        """Testa a operação de subtração"""
        self.assertEqual(calculadora_v2(5, 3, "-"), 2)
        self.assertEqual(calculadora_v2(-1, 1, "-"), -2)
        self.assertEqual(calculadora_v2(0, 0, "-"), 0)
        self.assertEqual(calculadora_v2(2.5, 1.5, "-"), 1.0)

    # def test_multiplicacao(self):
    #     """Testa a operação de multiplicação"""

    # def test_divisao(self):
    #     """Testa a operação de divisão"""
    #     self.assertEqual(calculadora_v2(6, 2, "/"), 3)

    #     # Teste de divisão por zero deve lançar ZeroDivisionError
    #     with self.assertRaises(ZeroDivisionError):
    #         calculadora_v2(5, 0, "/")

    # def test_modulo(self):
    #     """Testa a operação de módulo"""
    #     self.assertEqual(calculadora_v2(7, 3, "%"), 1)

    #     # Teste de módulo por zero deve lançar ZeroDivisionError
    #     with self.assertRaises(ZeroDivisionError):
    #         calculadora_v2(5, 0, "%")

    # def test_potencia(self):
    #     """Testa a operação de potência"""

    def test_operador_invalido(self):
        """Testa operador inválido"""
        self.assertTrue(math.isnan(calculadora_v2(5, 3, "x")))
        self.assertTrue(math.isnan(calculadora_v2(5, 3, "&")))
        self.assertTrue(math.isnan(calculadora_v2(5, 3, "")))

if __name__ == '__main__':
    unittest.main()

# para correr os testes: python -m unittest -v test_calculadora_alunos.py
