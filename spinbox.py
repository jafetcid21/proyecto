from tkinter import ttk
import tkinter as tk

def cambio_de_temperatura():
    temp = float(spin_temp.get()[:2])
    if temp <= 17:
        consumo = "Bajo"
    elif temp <= 24:
        consumo = "Medio"
    elif temp <= 30:
        consumo = "Alto"
    etiqueta_consumo["text"] = f"Consumo de energía: {consumo}."
    
ventana = tk.Tk()
ventana.config(width=300, height=200)
ventana.title("Termostato")

etiqueta_temp = ttk.Label(text="Temperatura:")
etiqueta_temp.place(x=20, y=30, width=100)
etiqueta_consumo = ttk.Label()
etiqueta_consumo.place(x=20, y=80)
spin_temp = ttk.Spinbox(from_=10, to=30, increment=0.5, format="%.1fºC",command=cambio_de_temperatura)

spin_temp.insert(0, "10ºC")
spin_temp["state"] = "readonly"
cambio_de_temperatura()
spin_temp.place(x=105, y=30, width=70)


ventana.mainloop()









ventana.mainloop()