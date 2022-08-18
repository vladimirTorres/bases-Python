# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("Estoy apendiendo a usar funcines!")

# imprimir_mensaje()
# imprimir_mensaje()

# print("Mensaje especial: ")
# print("Estoy apendiendo a usar funcines!")
# print("Mensaje especial: ")
# print("Estoy apendiendo a usar funcines!")

def conversacion(mensaje):
    print("Hola")
    print("Cómo estás")
    print(mensaje)
    print("Adios")

menu = int(input("Elige un menu (1, 2, 3): "))

if menu == 1:
    conversacion("Elegiste el menu 1")
elif menu == 2:
    conversacion("Elegiste el menu 2")
elif menu == 3:
    conversacion("Elegiste el menu 3")
else:
    print("Elije la opcion correcta")