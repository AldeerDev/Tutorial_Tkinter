import tkinter as tk

ventana = tk.Tk()
ventana.title('Spinbox avanzado')
ventana.geometry('300x200')

numero = tk.IntVar()

def mostrar():
    print('Valor actual:', numero.get())

# Spinbox con rango de números
spin1 = tk.Spinbox(
    ventana,
    from_=1,
    to=20,
    increment=2,
    textvariable=numero,
    command=mostrar,
    width=10
)
spin1.pack(pady=10)

# Spinbox con lista personalizada
opciones = ('Rojo', 'Azul', 'Verde', 'Amarillo')
color = tk.StringVar()

spin2 = tk.Spinbox(
    ventana,
    values=opciones,
    textvariable=color,
    width=15,
    command=lambda: print('Color:', color.get())
)
spin2.pack(pady=10)

ventana.mainloop()