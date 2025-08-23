import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title('Messagebox avanzado')

def salir():
    respuesta = messagebox.askyesno('Confirmar salida', '¿Deseas salir?')
    if respuesta:
        ventana.destroy()

btn_info = tk.Button(ventana, text='Info')
btn_info.config(command=lambda: messagebox.showinfo('Info', 'Mensaje informativo'))
btn_info.pack(pady=10)

btn_error = tk.Button(ventana, text='Error')
btn_error.config(command=lambda: messagebox.showerror('Error', 'Ha ocurrido un error.'))
btn_error.pack(pady=10)

btn_salir = tk.Button(ventana, text='Salir', command=salir)
btn_salir.pack(pady=10)

ventana.mainloop()