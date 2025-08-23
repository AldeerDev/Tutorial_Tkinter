# Checkbutton en Tkinter

El widget `Checkbutton` se usa para crear casillas de verificación.
Permite que el usuario marque o desmarque una opción, y puede haber varias casillas activadas al mismo tiempo.

## Sintaxis básica

```python
tk.Checkbutton(master, opciones)
```

- **master:** ventana o contenedor donde se coloca el Checkbutton.
- **opciones:** parámetros como texto, variable asociada, color, etc.

## Opciones más comunes

- **text:** Texto mostrado al lado de la casilla.
- **variable:** Variable asociada (IntVar, BooleanVar, StringVar).
- **onvalue:** Valor de la variable cuando está marcada.
- **offvalue:** Valor de la variable cuando está desmarcada.
- **command:** Función que se ejecuta cuando se cambia de estado.
- **fg:** Color de texto.
- **bg:** Color de fondo.
- **font:** Tipo y tamaño de letra.

## Ejemplo básico

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejemplo Checkbutton')

opcion = tk.IntVar()

check = tk.Checkbutton(ventana, text='Aceptar términos', variable=opcion)
check.pack()

def mostrar():
    if opcion.get() == 1:
        print('Casilla marcada')
    else:
        print('Casilla desmarcada')

boton = tk.Button(ventana, text= 'Mostrar estado', command=mostrar)
boton.pack()

ventana.mainloop()
```

## Ejemplo avanzado con varias casillas

```python
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
```