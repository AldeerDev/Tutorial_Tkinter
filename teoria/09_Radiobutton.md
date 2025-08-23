# Radiobutton en Tkinter

El widget `Radiobutton` permite crear botones de opción.
Se usa cuando el usuario debe elegir **una sola opción entre varias**.

## Sintaxis básica

```python
tk.Radiobutton(master, opciones)
```

- **master:** ventana o contenedor donde se coloca el Radiobutton.
- **opciones:** parámetro como texto, valor, variable asociada, etc.

## Opciones más comunes

- **text:** texto mostrado al lado del botón.
- **variable:** variable compartida entre todos los Radiobutton (generalmente IntVar o StringVar).
- **value:** valor que toma la variable cuando Radiobutton está seleccionado.
- **command:** función que se ejecuta cuando se selecciona.
- **fg:** Color de texto.
- **bg:** Color de fondo.
- **font:** tipo y tamaño de letra

## Ejemplo básico

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejemplo Radiobutton')

opcion = tk.StringVar()
opcion.set('Python') # Valor inicial

tk.Radiobutton(ventana, text='Python', variable=opcion, value='Python').pack(anchor='w')
tk.Radiobutton(ventana, text='Java', variable=opcion, value='Java').pack(anchor='w')
tk.Radiobutton(ventana, text='C++', variable=opcion, value='C++').pack(anchor='w')

def mostrar():
    print('Opción elegida:', opcion.get())

boton = tk.Button(ventana, text='Mostrar selección', command=mostrar)
boton.pack(pady=10)

ventana.mainloop()
```

## Ejemplo avanzado con estilos y acción inmediata

```python
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
```
