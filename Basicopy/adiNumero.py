import random


def run():
    numeroAleatorio = random.randint(1, 100)
    numeroElegido = int(input("Elege un numero del 1 al 100: "))
    while numeroElegido != numeroAleatorio:
        if numeroElegido < numeroAleatorio:
            print("Busca un numero mas grnde")
        else:
            print("Busca un numero mas pequeño")
        numeroElegido = int(input("Elige otro numero: "))
    print("¡Ganaste!")


if __name__ == "__main__":
    run()