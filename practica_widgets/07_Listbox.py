import tkinter as tk

ventana = tk.Tk()
ventana.title('Listbox Avanzado')
ventana.geometry('300x300')

lista = tk.Listbox(ventana, selectmode='multiple', bg='lightyellow', font=('Arial', 12))
lista.pack(pady=10, fill='both', expand=True)

# Agregar elementos
lenguajes = ['Python', 'Java', 'C++', 'JavaScript']
for item in lenguajes:
  lista.insert(tk.END, item)

def mostrar():
  seleccion = lista.curselection()
  if seleccion:
    elegidos = [lista.get(i) for i in seleccion]
    print('Seleccionados:', ', '.join(elegidos))

def limpiar():
  lista.selection_clear(0, tk.END)

boton1 = tk.Button(ventana, text='Mostrar selección', command=mostrar)
boton1.pack(pady=5)

boton2 = tk.Button(ventana, text='Limpiar selección', command=limpiar)
boton2.pack(pady=5)

ventana.mainloop()