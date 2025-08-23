import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Combobox avanzado')
ventana.geometry('300x150')

lenguaje = tk.StringVar()

def mostrar(evento):
    print('Seleccionaste:', lenguaje.get())

opciones = ['Python', 'Java', 'C++', 'JavaScript']

combo = ttk.Combobox(
    ventana,
    textvariable=lenguaje,
    values=opciones,
    state='readonly',
    width=20
)
combo.current(0)
combo.pack(pady=10)

# evento que detecta cuando el usuario selecciona algo
combo.bind('<<ComboboxSelected>>', mostrar)

ventana.mainloop()