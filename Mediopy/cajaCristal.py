import unittest

def esMayorDeEdad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    
    def testEsMayorDeEdad(self):
        edad = 20

        resultado = esMayorDeEdad(edad)

        self.assertEqual(resultado, True)

    def testEsMenorDeEdad(self):
        edad = 15

        resultado = esMayorDeEdad(edad)

        self.assertEqual(resultado, False)


if __name__ == "__main__":
    unittest.main()