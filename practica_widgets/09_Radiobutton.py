import tkinter as tk

ventana = tk.Tk()
ventana.title('Radiobutton avanzado')
ventana.geometry('300x300')

lenguaje = tk.StringVar()
lenguaje.set('Python') # valor incial

def mostrar():
    print('Seleccionaste:', lenguaje.get())

opciones = ['Python', 'Java', 'C++', 'JavaScript']

for opcion in opciones:
    tk.Radiobutton(
        ventana,
        text=opcion,
        variable=lenguaje,
        value=opcion,
        command=mostrar,
        font=('Arial', 12),
        bg='lightyellow'
    ).pack(anchor='w', pady=2)

ventana.mainloop()