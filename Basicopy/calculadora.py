from tkinter import *
from math import *

# Funcion visualizar pantalla
def botonClik(num):
    global operador
    operador = operador + str(num)
    input_text.set(operador)

# Funcion calculo y resultado
def resultado():
    global operador
    try:
        opera = str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""

# Funcion limpieza de pantalla
def clear():
    global operador
    operador = ("")
    input_text.set("0")

calculadora = Tk()
calculadora.title("3-calculadora-gjse")

calculadora.geometry("400x530")
calculadora.configure(background="purple")
color_boton = ("pink")

ancho_boton1 = 50
alto_boton1 = 2
ancho_boton = 11
alto_boton = 3
input_text = StringVar()
operador = ""

Salida = Entry(calculadora, font = ("Comic Sans MS", 20, "bold"), width = 19, 
textvariable=input_text, bd = 20, insertwidth=6, bg="powder blue", justify="right")
Salida.place(x=22,y=60)

# Crear Botones
Button(calculadora, text="0", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik(0)).place(x=17,y=420)
Button(calculadora, text="1", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik(1)).place(x=197,y=360)
Button(calculadora, text="2", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik(2)).place(x=107,y=360)
Button(calculadora, text="3", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik(3)).place(x=17,y=360)
Button(calculadora, text="4", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik(4)).place(x=197,y=300)
Button(calculadora, text="5", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik(5)).place(x=107,y=300)
Button(calculadora, text="6", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik(6)).place(x=17,y=300)
Button(calculadora, text="7", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik(7)).place(x=197,y=240)
Button(calculadora, text="8", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik(8)).place(x=107,y=240)
Button(calculadora, text="9", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik(9)).place(x=17,y=240)
Button(calculadora, text=",", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik(".")).place(x=107,y=420)
Button(calculadora, text="+", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik("+")).place(x=287,y=420)
Button(calculadora, text="-", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik("-")).place(x=287,y=360)
Button(calculadora, text="*", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik("*")).place(x=287,y=300)
Button(calculadora, text="/", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik("/")).place(x=287,y=240)
Button(calculadora, text="√", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik("sqrt")).place(x=107,y=180)
Button(calculadora, text="(", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik("(")).place(x=197,y=180)
Button(calculadora, text=")", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:botonClik(")")).place(x=287,y=180)
Button(calculadora, text="C", bg=color_boton, width=ancho_boton, height=alto_boton, command=clear).place(x=17,y=180)
Button(calculadora, text="=", bg=color_boton, width=ancho_boton, height=alto_boton, command=resultado).place(x=197,y=420)
Button(calculadora, text="VTV-2022", bg=color_boton, width=ancho_boton1, height=alto_boton1, command=lambda:botonClik("Vladimir Torres")).place(x=17,y=480)

clear()

calculadora.mainloop()