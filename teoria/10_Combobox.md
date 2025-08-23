## Combobox en Tkinter (ttk)

El widget `Combobox` (perteneciente a `ttk`) Se utiliza para mostrar una **lista desplegable** de opciones, en la que el usuario puede seleccionar un valor.
Opcionalmente, también se puede escribir diractamente en el campo.

## Importante
Para usar `Combobox` debemos importar desde `tkinter.ttk`

```python
from tkinter import ttk
```

## Sintaxis básica
```python
ttk.Combobox(master, opciones)
```

- **master:** ventana o contenedor.
- **opciones:** parámetros como lista de valores, texto inicial, ancho, etc.

## Opciones más comunes

- **values:** Lista de valores que se mostrarán en el Combobox.
- **state:**
  - "normal" permite escribir y seleccionar.
  - "readonly" solo perimte seleccionar de la lista.
- **width:** Ancho del Combobox.
- **textvariable:** Variable asociada (ej. StrinVar).
- **current:** Define el valor seleccionado inicialmente.

## Ejemplo básico

```python
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Ejemplo Combobox')

opciones = ['Python', 'Java', 'C++', 'JavaScript']

combo = ttk.Combobox(ventana, values=opciones)
combo.current(0)
combo.pack(pady=10)

ventana.mainloop()
```

## Ejemplo avanzado con variable y evento

```python
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Combobox avanzado')
ventana.geometry('300x150')

lenguaje = tk.StringVar()

def mostrar():
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
```
