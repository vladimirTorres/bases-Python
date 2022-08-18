# Datos obtenidos
print("Ingrese los datos del empleado")
numeroDeIdentificacion = int(input("Numero de identificacion: "))
nombres = input("Nombres: ")
apellidos = input("Apellidos: ")
direccion = input("Direccion: ")
telefono = int(input("Telefono: "))
edad = int(input("Edad: "))
genero = input("Genero: ")
estadoCivil = input("Estado civil: ")
numeroDeHijos = int(input("Numero de hijos: "))
estatura = float(input("Estaruta en metros: "))
fechaDeContrato = print("Fecha de contrato:")
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))
sueldoBasico = float(input("Sueldo basico: "))
diasLaborados = int(input("Cuantos dias laborado en el mes: "))

# Mostrar datos
print("*")
print("Datos del empleado")
print("*")
print("Numero de identificacion: ", numeroDeIdentificacion)
print("Nombres: ", nombres)
print("Apellidos: ", apellidos)
print("Direccion: ", direccion)
print("Telefono: ", telefono)
print("Edad: ", edad)
print("Genero: ", genero)
print("Estado civil: ", estadoCivil)
print("Numero de hijos: ", numeroDeHijos)
print("Estaruta: ", estatura, " metros")
print("Fecha de contrato: ", dia, "/", mes, "/", año)
print("Sueldo basico: ", sueldoBasico)
print("Dias laborados en el mes: ", diasLaborados)

# Fase 2

fechaDeNacimiento = print("Fecha de nacimiento:")
diaN = int(input("Ingrese el dia: "))
mesN = int(input("Ingrese el mes: "))
añoN = int(input("Ingrese el año: "))

bono = (sueldoBasico * 5) / 100

#Si el empleado es mayor de 55 años disfrutará de un bono de prepensión
#correspondiente al 5% de su sueldo básico.
if edad > 55:
    print("Felicitaciones tienes ", edad, "años ", "tienes un bono de: ", bono, " pesos")
else:
    print("No eres mayor de edad para el bono")

#Si el día de nacimiento del empleado coincide con el día de la fundación de
#la compañía, se le realizará una fiesta.
if diaN == 23 and mesN == 6:
    print("Felicitaciones la fecha de tu cumpleaños coincide con la fundacion de la empresa")
else:
    print("La fecha de cumpleaños no coincide con la fundacion de la empresa")

# Si el empleado es casado y tiene hijos se le otorgará un paseo cada
# diciembre
if estadoCivil == "casado" and numeroDeHijos > 1:
    print("Felicitaciones tiene un paseo cada diciembre")
else:
    print("No cumpre con los requisitos para el paseo en diciembre")

# Si el sueldo básico está entre 1000000 y 1500000 tendrá una comisión del
# 2% sobre el valor del sueldo; Si el sueldo básico está entre 1500001 y
# 2000000 tendrá una comisión del 5% sobre el valor del sueldo; para todos
# los demás casos no habrá comisión.
if sueldoBasico >= 100000 and sueldoBasico <= 1500000:
    comision1 = (sueldoBasico *2) / 100
    print("Tiene una comicion de: ", comision1, "pesos")
elif sueldoBasico >= 1500001 and sueldoBasico <= 2000000:
    comision2 = (sueldoBasico *5) / 100
    print("Tiene una comicion de: ", comision2, "pesos")
else:
    print("No cumpre los requisitos para la comision")

# Si el empleado trabajó más de 20 días al mes y su sueldo es menor a
# 1000000 tendrá derecho a un bono de alimentación.
if diasLaborados > 20 and sueldoBasico < 1000000:
    print("Tiene derecho a un bono de alimentacion")
else:
    print("No cumple los requisitos para bono de alimentacion")

# Fase 3

for edad in range(18,63,1):
    print(edad)

