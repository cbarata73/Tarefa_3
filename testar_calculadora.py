import unittest
import math
from calculadora import calculadora_v2, calculadora

class TestCalculadoraV2(unittest.TestCase):
    def test_adicao(self):
        """Testa a operação de adição"""
        self.assertEqual(calculadora_v2(5, 3, "+"), 8)
        self.assertEqual(calculadora_v2(-1, 1, "+"), 0)
        self.assertEqual(calculadora_v2(0, 0, "+"), 0)
        self.assertEqual(calculadora_v2(1.5, 2.5, "+"), 4.0)
        self.assertEqual(calculadora(5, 3, "+"), 8)
        self.assertEqual(calculadora(-1, 1, "+"), 0)

    def test_subtracao(self):
        """Testa a operação de subtração"""
        self.assertEqual(calculadora_v2(5, 3, "-"), 2)
        self.assertEqual(calculadora_v2(-1, 1, "-"), -2)
        self.assertEqual(calculadora_v2(0, 0, "-"), 0)
        self.assertEqual(calculadora_v2(2.5, 1.5, "-"), 1.0)

    def test_multiplicacao(self):
        """Testa a operação de multiplicação"""
        self.assertEqual(calculadora_v2(5, 3, "*"), 15)
        self.assertEqual(calculadora_v2(-2, 3, "*"), -6)
        self.assertEqual(calculadora_v2(0, 5, "*"), 0)
        self.assertEqual(calculadora_v2(2.5, 2, "*"), 5.0)

    def test_divisao(self):
        """Testa a operação de divisão"""
        self.assertEqual(calculadora_v2(6, 2, "/"), 3)
        self.assertEqual(calculadora_v2(-6, 2, "/"), -3)
        self.assertEqual(calculadora_v2(5, 2, "/"), 2.5)
        # Teste de divisão por zero deve lançar ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            calculadora_v2(5, 0, "/")

    def test_modulo(self):
        """Testa a operação de módulo"""
        self.assertEqual(calculadora_v2(7, 3, "%"), 1)
        self.assertEqual(calculadora_v2(10, 2, "%"), 0)
        self.assertEqual(calculadora_v2(5.5, 2, "%"), 1.5)
        # Teste de módulo por zero deve lançar ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            calculadora_v2(5, 0, "%")

    def test_potencia(self):
        """Testa a operação de potência"""
        self.assertEqual(calculadora_v2(2, 3, "^"), 8)
        self.assertEqual(calculadora_v2(3, 2, "^"), 9)
        self.assertEqual(calculadora_v2(2, 0, "^"), 1)
        self.assertEqual(calculadora_v2(5, 1, "^"), 5)

    def test_operador_invalido(self):
        """Testa operador inválido"""
        self.assertTrue(math.isnan(calculadora_v2(5, 3, "x")))
        self.assertTrue(math.isnan(calculadora_v2(5, 3, "&")))
        self.assertTrue(math.isnan(calculadora_v2(5, 3, "")))

if __name__ == '__main__':
    unittest.main()

# para correr os testes: python -m unittest -v testar_calculadora.py
