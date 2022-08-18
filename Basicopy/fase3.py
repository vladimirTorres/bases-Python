# Datos obtenidos
mayorNumeroHijos = 0
nominaToTal = 0
menorDiasLab = 0
solteros = 0
jubilacionH = 0
jubilacionM = 0

cantidad = int(print("Ingrese cuantos empleados de la empresa quiere validar: "))

# Mostrar datos
for i in range(cantidad):
    nombre = input("Ingrese el nombre del empleado: ")

    edad = int(input("Edad del empleado: "))
    while edad < 18 and edad > 63:
        print("Edad incorrecta fuera del rango, valide nuevamente")
        edad = int(input("Edad del empleado: "))

    genero = input("Cuel es el genero (M/F): ")
    while genero != "M" and genero != "F":
        print("Genedo distinto al solicitado! intente de nuevo")
        genero = input("Cuel es el genero (M/F): ")

    altura = float(input("Altura del empleado en metros: "))
    while altura < 1 and altura > 3:
        print("Altura fuera de rango! intente de nuevo")
        altura = float(input("Altura del empleado en metros: "))

    estadoCivil = input("Cual es su estado civil: ")
    while estadoCivil.title() != "Soltero" and estadoCivil.title() != "Casado" and estadoCivil.title() != "Separado":
        print("Estado civil distinto al solicitado! intente de nuevo")
        estadoCivil = input("Cual es su estado civil: ")

    numeroHijos = int(input("Ingrese numero de hijos del empleado: "))
    while numeroHijos < 0:
        print("Valor invalido, el numero de hijos del empleado es menor a 0")
        numeroHijos = int(input("Ingrese numero de hijos del empleado: "))
    if numeroHijos > mayorNumeroHijos:
        mayorNumeroHijos = numeroHijos
        empConMasHijos = nombre

    sueldo = int(input("Ingrese el sueldo basico del empleado: "))
    while sueldo <= 0:
        print("Valor invalido, el sueldo del empleado es menor a 0")
        sueldo = int(input("Ingrese el sueldo basico del empleado: "))
    nominaToTal = nominaToTal + sueldo

    diasLab = int(input("Ingrese el numero de dias laborados del empleado: "))
    while diasLab < 0 or diasLab > 31:
        print("Valor invalido, el numero de dias laborados del empleado debe ser valido")
        diasLab = int(input("Ingrese el numero de dias laborados del empleado: "))
    if diasLab < menorDiasLab:
        menorDiasLab = diasLab