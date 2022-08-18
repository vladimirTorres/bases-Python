def conversor(tipo_peso, valor_dolar):
    pesos = float(input("Ingrese los pesos " + tipo_peso + " que tiene: "))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tiene $" + dolares + " dolares")

menu = """"
Buenbenidos al convertidor a dolares

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos chilenos
4 - Pesos mexicanos
5 - Otra moneda

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 4100)
elif opcion == 2:
    conversor("argentinos", 125)
elif opcion == 3:
    conversor("chilenos", 932)
elif opcion == 4:
    conversor("mexicanos", 20)
elif opcion == 5:
    print("No tenemos otra opcion de moneda")
else:
    print("Ingresa una opcion valida")


# pesos = float(input("Ingrese los pesos colombianos: "))
# valor_dolar = 4100
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("En dolares Tienes $" + dolares + " dolares") 