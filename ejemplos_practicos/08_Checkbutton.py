import tkinter as tk

ventana = tk.Tk()
ventana.title('Checkbutton avanzados')
ventana.geometry('300x300')

# Variables asociadas
python = tk.BooleanVar()
java= tk.BooleanVar()
cpp = tk.BooleanVar()

def mostrar():
    seleccionados = []
    if python.get():
        seleccionados.append('Python')
    if java.get():
        seleccionados.append('Java')
    if cpp.get():
        seleccionados.append('C++')
    print('Seleccionados:', ', '.join(seleccionados) if seleccionados else 'Ninguno')

tk.Checkbutton(ventana, text='Python', variable=python).pack(anchor='w')
tk.Checkbutton(ventana, text='Java', variable=java).pack(anchor='w')
tk.Checkbutton(ventana, text='C++', variable=cpp).pack(anchor='w')

boton = tk.Button(ventana, text='Mostrar seleccion', command=mostrar)
boton.pack(pady=10)

ventana.mainloop()