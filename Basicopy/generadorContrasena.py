import random

def generarContrasena():
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
    minuscula = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
    simbolos = ["!", "#", "$", "&", "/", "(", ")"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    caracteres = mayusculas + minuscula + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracterRandom = random.choice(caracteres)
        contrasena.append(caracterRandom)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generarContrasena()
    print("Tu nueva contraseña es: ", contrasena)


if __name__ == "__main__":
    run()