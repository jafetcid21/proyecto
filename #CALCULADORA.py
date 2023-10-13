#practica 1

from tkinter import*
from tokenize import Exponent

ventana = Tk();
ventana.title("calculadora")
ventana.configure(bg = 'dark red')
ventana.resizable(False,False)

e_texto = Entry(ventana, font = ("Calibri 30"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady=5)


i = 0
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0,END)
    i = 0

    
def opercacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0,END)
    e_texto.insert(0,resultado)
    

def exponencial(a,b):
    global i
    e_texto.insert(i, Exponent)
    i = i**1
    
    
boton1 = Button(ventana, text="1", width=10, height=2, bd=12, bg="grey", command=lambda:click_boton(1))
boton2 = Button(ventana, text="2", width=10, height=2, bd=12, bg="grey", command=lambda:click_boton(2))
boton3 = Button(ventana, text="3", width=10, height=2, bd=12, bg="grey", command=lambda:click_boton(3))
boton4 = Button(ventana, text="4", width=10, height=2, bd=12, bg="grey", command=lambda:click_boton(4))
boton5 = Button(ventana, text="5", width=10, height=2, bd=12, bg="grey", command=lambda:click_boton(5))
boton6 = Button(ventana, text="6", width=10, height=2, bd=12, bg="grey", command=lambda:click_boton(6))
boton7 = Button(ventana, text="7", width=10, height=2, bd=12, bg="grey", command=lambda:click_boton(7))
boton8 = Button(ventana, text="8", width=10, height=2, bd=12, bg="grey", command=lambda:click_boton(8))
boton9 = Button(ventana, text="9", width=10, height=2, bd=12, bg="grey", command=lambda:click_boton(9))
boton0 = Button(ventana, text="0", width=19, height=2, bd=12, bg="grey", command=lambda:click_boton(0))

boton_borrar = Button(ventana, text="AC", width=3, height=2, bd=12, bg="white", command=lambda:borrar())
boton_Parentesis1 = Button(ventana, text="(", width=2, height=2, bd=12, bg="white", command=lambda:click_boton("("))
boton_Parentesis2 = Button(ventana, text=")", width=3, height=2, bd=12, bg="white", command=lambda:click_boton(")"))
boton_EXPO = Button(ventana, text="EXP", width=3, height=2, bd=12, bg="white", command=lambda:click_boton("**"))

boton_div = Button(ventana, text="%", width=5, height=2, bd=12, bg="aqua", command=lambda:click_boton("/") )
boton_mult = Button(ventana, text="x", width=5, height=2, bd=12, bg="aqua", command=lambda:click_boton("*"))
boton_suma = Button(ventana, text="+", width=5, height=2, bd=12, bg="aqua", command=lambda:click_boton("+"))
boton_resta = Button(ventana, text="-", width=5, height=2, bd=12, bg="aqua", command=lambda:click_boton("-"))
boton_igual = Button(ventana, text="=", width=5, height=2, bd=12, bg="aqua", command=lambda:opercacion())

#asignamos colocacion de elementos en ventana
boton_borrar.grid(row=1, sticky=(W, E), column=0, padx=6, pady=5)
boton_Parentesis1.grid(row=1, sticky=(W, E), column=1, padx=5, pady=5)
boton_Parentesis2.grid(row=1, sticky=(W, E), column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, sticky=(W, E), padx=5, pady=5)

boton7.grid(row=2, column=0, sticky=(W, E), padx=5, pady=5)
boton8.grid(row=2, column=1, sticky=(W, E), padx=5, pady=5)
boton9.grid(row=2, column=2, sticky=(W, E), padx=5, pady=5)
boton_mult.grid(row=2, column=3, sticky=(W, E), padx=5, pady=5)

boton4.grid(row=3, column=0, sticky=(W, E), padx=5, pady=5)
boton5.grid(row=3, column=1, sticky=(W, E), padx=5, pady=5)
boton6.grid(row=3, column=2, sticky=(W, E), padx=5, pady=5)
boton_suma.grid(row=3, column=3, sticky=(W, E), padx=5, pady=5)

boton1.grid(row=4, column=0, sticky=(W, E), padx=5, pady=5)
boton2.grid(row=4, column=1, sticky=(W, E), padx=5, pady=5)
boton3.grid(row=4, column=2, sticky=(W, E), padx=5, pady=5)
boton_resta.grid(row=4, column=3, sticky=(W, E), padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, sticky=(W, E))
boton_EXPO.grid(row=5, column=2, padx=5, sticky=(W, E), pady=5)
boton_igual.grid(row=5, column=3, padx=5, sticky=(W, E), pady=5)

ventana.mainloop()
