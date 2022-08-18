# Datos ingresados por sistema
nombre = input("Digite el nombre del estudiante: ")
nombre = nombre.title()
nota1 = float(input("Digite la primera nota: "))
nota2 = float(input("Digite la segunda nota: "))
nota3 = float(input("Digite la tercera nota: "))

# Operaciones
promedio = (nota1 + nota2 + nota3) / 3

# Resultados
if promedio >= 3.5 and promedio <= 5:
    print("Estudiante ", nombre, " -PROMOCIONADO- ", "su nota es: ", promedio)
elif promedio >= 2.5 and promedio <= 3.4:
    print("Estudiante ", nombre, " -HACER PLAN DE MEJORAMIENTO- ", "su nota es: ", promedio)
elif promedio < 2.5:
    print("Estudiante ", nombre, " -REPROBADO- ", "su nota es: ", promedio)
else:
    print("NOTA INVALIDA")