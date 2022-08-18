def linea():
    print("*********************************************************************")

# Diccionario con 3 elementos
colores = {"1":"Azul","2":"Amarillo","3":"Rojo"}

# Mostrar elementos del diccionario
linea()
print(colores)

# Agregar elemtos al diccionario
colores[4] = "Verde"
colores[5] = "Naranja"

linea()
print(colores)

# Eliminar datos del diccionario
del colores[5]

linea()
print(colores)
linea()