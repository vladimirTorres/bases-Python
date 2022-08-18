import unittest

# Las pruevas de caja negra es importante importar unittest
# para hacer la clase y sus funciones de pruebas

def suma(numero1, numero2):
    return abs(numero1) + numero2

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        numero1 = 10
        numero2 = 5

        resultado = suma(numero1, numero2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num1 = -10
        num2 = -7

        resultado = suma(num1, num2)

        self.assertEqual(resultado, -17)

if __name__ == "__main__":
    unittest.main()