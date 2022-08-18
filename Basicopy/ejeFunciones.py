def suma(num1, num2):
    sumar = num1 + num2
    return sumar

def resta(num1, num2):
    restar = num1 - num2
    return restar

def multiplicacion(num1, num2):
    por = num1 * num2
    return por

def division(num1, num2):
    dividir = num1 / num2
    return dividir

def linea():
    print("******************************************")

valor1 = int(input("Ingrese un numero: "))
valor2 = int(input("Ingrese otro numero: "))

print("La suma de ", valor1, "+", valor2, "es: ", suma(valor1, valor2))
linea()
print("La resta de ", valor1, "-", valor2, "es: ", resta(valor1, valor2))
linea()
print("La multiplicacion es ", valor1, "*", valor2, "es: ", multiplicacion(valor1, valor2))
linea()
print("La division de ", valor1, "/", valor2, "es: ", division(valor1, valor2))

def suma2():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("sumado con: "))
    suma = num1 + num2
    print("La suma es: ", suma)

def resta2():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("estado con: "))
    resta = num1 - num2
    print("La resta es: ", resta)

def multiplicacion2():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("multiplicado con: "))
    multiplicacion = num1 * num2
    print("La multiplicacion es: ", multiplicacion)

def division2():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("dividido con: "))
    division = num1 / num2
    print("La division es: ", division)

linea()
suma2()
linea()
resta2()
linea()
multiplicacion2()
linea()
division2()