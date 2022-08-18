from tkinter import *

# formulario = Tk()
# formulario.title("Mi primer formulario")
# formulario.geometry("400x200")
# formulario.config(bg="blue")
# formulario.resizable(0,0)

formulario = Tk()
formulario.title("Suma de numeros")
formulario.geometry("400x200")

def sumar():
    primero = int(caja1.get())
    segundo = int(caja2.get())
    sumar = (primero + segundo)
    return variable1.set(sumar)

variable1 = StringVar()

etiqueta1 = Label(formulario, text="Suma de numeros")
etiqueta1.config(font=("Arial", 16))
etiqueta2 = Label(formulario, text="Ingrese primer numero")
caja1 = Entry(formulario, text="primer numero")
etiqueta3 = Label(formulario, text="Ingrese el segundo numero")
caja2 = Entry(formulario, text="segundo numero")
boton1 = Button(formulario, text="Suma", command=sumar)
etiqueta4 = Label(formulario, text="El resultado de la suma es")
caja3 = Entry(formulario, textvariable=variable1)
etiqueta5 = Label(formulario, textvariable=variable1)

etiqueta1.pack()
etiqueta2.pack()
caja1.pack()
etiqueta3.pack()
caja2.pack()
boton1.pack()
etiqueta4.pack()
caja3.pack()
etiqueta5.pack()

formulario.mainloop()