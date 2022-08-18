# Datos ingresados por sistema
nombre = input("Digite el nombre del estudiante: ")
nombre = nombre.title()
nota1 = float(input("Digite la primera nota: "))
nota2 = float(input("Digite la segunda nota: "))
nota3 = float(input("Digite la tercera nota: "))
nota4 = float(input("Digite la cuarta nota: "))

# Operaciones
promedio = (nota1 + nota2 + nota3 + nota4) / 4
suma = nota1 + nota4
multiplicacion = nota2 + nota3


# Resultados
print("------------------------------------------------------------------------------")
print("Nombre del estudiante: ", nombre, " Nota definitiva de matimaticas es: ", promedio)
print("------------------------------------------------------------------------------")
print("La suma de la primera nota: ", nota1, " y cuarta nota: ", nota4, " Es: ", suma)
print("------------------------------------------------------------------------------")
print("La multiplicacion de la segunda nota: ", nota2, " y tercera nota: ", nota3, " Es: ", multiplicacion)