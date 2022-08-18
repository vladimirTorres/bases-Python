
nombres = []
edad = []
direccion = []
telefono = []

clientes = int(input("Cuantos clientes va a ingresar: "))

for x in range(clientes):
    nombre = input("Digite el nombre del cliente: ")
    nombres.append(nombre.title())
    ed = int(input("Ingrese la edad: "))
    edad.append(ed)
    direc = input("Ingrese la direccion: ")
    direccion.append(direc)
    tel = int(input("Ingrese el telefono: "))
    telefono.append(tel)

print(nombres[0], edad[0], direccion[0], telefono[0])

print(nombres)
print(edad)
print(direccion)
print(telefono)