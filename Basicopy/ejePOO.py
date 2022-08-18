class Estudiante:
    def __init__(self):
        print("Datos del estudiante")
        self.nombre = input("Ingrese nombre del estudiante: ")
        self.carrera = input("Ingrese la carrera que esta estudiando: ")
        self.precio = float(input("Cual es el precio de la carrera: "))
        self.edad = int(input("Ingrese la edad del estudiante: "))
        
    def imprimir(self):
        print("El nombre es: ", self.nombre.title())
        print("La carrera que esta estudiando es: ", self.carrera)
        print("El precio de la carrera es: ", self.precio)
        print("La edad del estudiante es: ", self.edad)

# principal
print("Primer estudiante(Objeto1)")
estudiante1 = Estudiante()
estudiante1.imprimir()
print("Segundo estudiante(Objeto2)")
estudiante2 = Estudiante()
estudiante2.imprimir()

class Motos:
    def __init__(datos):
        print("Datos de la moto")
        datos.marca = input("Ingrese marca de la moto: ")
        datos.color = input("Ingrese el color: ")
        datos.modelo = int(input("Cual es modelo: "))
        
        
    def imprimir(dato):
        print("La marca es: ", dato.marca.title())
        print("El color de la moto: ", dato.color)
        print("El modelo de la moto: ", dato.modelo)

# principal
print("Objeto1")
moto1 = Motos()
moto1.imprimir()
print("Objeto2")
moto2 = Motos()
moto2.imprimir()