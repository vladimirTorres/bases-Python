# Crear un programa que tenga un arreglo con el nombre numeros que almacene 5 enteros, 
# Sumar todos sus elementos y mostrar dicha suma.
def linea():
    print("******************************************************")

# Operaciones
numeros = [1,2,3,4,5]
suma = 0
x = 0

while x < len(numeros):
    suma = suma + numeros[x]
    x = x + 1

# Resultados
linea()
print("Los numeros son: ", numeros)
print("La suma de todos los numeros es: ", suma)
linea()

# Crear un programa con un Arrays que almacene en el primer componente o lugar el nombre 
# de un alumno y en las dos siguientes sus notas. Imprimir luego el nombre y el promedio 
# de las dos notas.

# Datos ingresados por sistema
nombre = input("Ingrese el Nombre el alumno: ")
nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))

# Operaciones
alumno = [nombre.title(),nota1,nota2]
promedio = (alumno[1] + alumno[2]) / 2

# Resultados
print("Nombre del alumno: ", alumno)
print("Promedio de las dos notas: ", promedio)
linea()

# Realizar la carga de valores enteros por teclado, almacenarlos en un Arrays. Finalizar 
# la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño del Arrays.

# Datos ingresados por sistema
sueldos = []
datos = int(input("Ingrese datos para finalizar ingrese 0: "))
while datos != 0:
    sueldos.append(datos)
    datos = int(input("Ingrese datos para finalizar ingrese 0: "))

# Resultados
print("Tamaño del arrays es de : ", len(sueldos), " elementos")
linea()

# Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados 
# (4 por la mañana y 4 por la tarde). Crear un programa que permita almacenar los sueldos 
# de los empleados agrupados en dos listas e Imprima o muestre las dos listas de sueldos.

# Datos ingresados por sistema
sueldosM = []
print("Sueldos turno mañana")

for x in range(4):
    valor = float(input("Ingrese sueldo: "))
    sueldosM.append(valor)

sueldosT = []
print("Sueldos turno Tarde: ")

for x in range(4):
    valor = float(input("Ingrese sueldo: "))
    sueldosT.append(valor)

# Resultados
print("Turno mañana: ", sueldosM)
print("Turno tarde: ", sueldosT)
linea()

# Realizar un Programa que sume, reste, multiplique y divida 2 matrices, el usuario debe 
# ingresa el tamaño de las matrices e ingresar los elementos de cada matriz. El programa 
# debe mostrar las Matrices resultantes con las suma, resta, multiplicación y división.

# Datos ingresados por sistema
# esto es para solicitar el tamaño de columnas y filas
colum = int(input("Ingrese el numero de columnas: "))
fila = int(input("Ingrese el numero de fila: "))

# Se declara las matrices
matriz1 = [[0 for i in range(colum)] for j in range(fila)]
matriz2 = [[0 for i in range(colum)] for j in range(fila)]
matrizS = [[0 for i in range(colum)] for j in range(fila)]
matrizR = [[0 for i in range(colum)] for j in range(fila)]
matrizM = [[0 for i in range(colum)] for j in range(fila)]
matrizD = [[0 for i in range(colum)] for j in range(fila)]

# Se ingresan los valores de la matriz 1
for i in range(fila):
    for j in range(colum):
        matriz1[i][j] = int(input("Ingrese los valores de la matriz 1: "))

# Se ingresan los valores de la matriz 2
for i in range(fila):
    for j in range(colum):
        matriz2[i][j] = int(input("Ingrese los valores de la matriz 2: "))

# Se realizan las operaciones con el ciclo for
for i in range(fila):
    for j in range(colum):
        matrizS [i][j] = matriz1[i][j] + matriz2[i][j]
        matrizR [i][j] = matriz1[i][j] - matriz2[i][j]
        matrizM [i][j] = matriz1[i][j] * matriz2[i][j]
        matrizD [i][j] = matriz1[i][j] / matriz2[i][j]

# Resultados
# Se imprime el resultado de cada matriz
print("El resultado de la suma de las matrices es: ")
print(matrizS)
print("El resultado de la resta de las matrices es: ")
print(matrizR)
print("El resultado de la multiplicacion de las matrices es: ")
print(matrizM)
print("El resultado de la divicion de las matrices es: ")
print(matrizD)