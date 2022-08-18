class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese nombre: ")
        self.apellido = input("Ingrese apellido: ")
        self.direccion = input("Ingrese direccion: ")
        self.telefono = int(input("Ingrese el telefono: "))

    def imprimir(self):
        print("El nombre es: ", self.nombre.title())
        print("El apellido es: ", self.apellido.title())
        print("La direccion es: ", self.direccion)
        print("El telefono es: ", self.telefono)

    def generos(self):
        self.genero = input("Ingrese el genero del empleado: ")
        self.genero = self.genero.title()
        while self.genero != "Femenino" and self.genero != "Masculino":
            print("La opcion es incorrecta!")
            self.genero = input("Ingrese el genero del empleado: ")
            self.genero = self.genero.title()

    def edades(self):
        self.edad = int(input("Ingrese la edad del empleado para la fiesta: "))
        print("Debe ser mayor de 18 años")
        if self.edad < 18:
            print("No puedes ir a la fiesta")
        else:
            print("Felicitaciones puedes ir a la fiesta")

# principal
print("Primer empleado(Objeto1)")
empleado1 = Empleado()
empleado1.imprimir()
empleado1.generos()
empleado1.edades()
print("Segundo empleado(Objeto2)")
empleado2 = Empleado()
empleado2.imprimir()
empleado2.generos()
empleado2.edades()