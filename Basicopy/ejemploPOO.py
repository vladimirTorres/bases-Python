class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese nombre: ")
        self.sueldo = int(input("Ingrese el sueldo: "))

    def imprimir(self):
        print("El nombre es: ", self.nombre)
        print("El sueldo es: ", self.sueldo)

    def paga_impuesto(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuesto")

# principal
print("Primer empleado(Objeto1)")
empleado1 = Empleado()
empleado1.imprimir()
empleado1.paga_impuesto()
print("Segundo empleado(Objeto2)")
empleado2 = Empleado()
empleado2.imprimir()
empleado2.paga_impuesto()

class Operaciones:
    def __init__(identificador):
        identificador.valor1 = int(input("Ingrese primer numero: "))
        identificador.valor2 = int(input("Ingrese segundo numero: "))

    def Sumar(identificador):
        suma = identificador.valor1 + identificador.valor2
        print("La suma es: ", suma)

    def Restar(identificador):
        resta = identificador.valor1 - identificador.valor2
        print("La resta es: ", resta)

    def Multiplicar(identificador):
        multi = identificador.valor1 * identificador.valor2
        print("La multiplicacion es: ", multi)

    def Division(identificador):
        divi = identificador.valor1 / identificador.valor2
        print("La division es: ", divi)

# bloque
objeto1 = Operaciones()
objeto1.Sumar()
objeto1.Restar()
objeto1.Multiplicar()
objeto1.Division()