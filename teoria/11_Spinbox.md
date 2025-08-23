# Spinbox en Tkinter

El widget `Spinbox` permite al usuario seleccionar un valor de una **secuencia numérica** o de una **lista de opciones predefinidas**.
Funciona como un campo de entrada con flechas arriba/abajo.

## Sintaxis básica

```python
tk.Spinbox(master, opciones)
```

- **master:** ventana o contenedor donde se coloca.
- **opciones:** rango de valores, incremento, texto inicial, etc.

## Opciones más comunes

- **from_:** valor mínimo.
- **to:** valor máximo.
- **increment:** Paso entre los valores (por defecto 1).
- **values:** Variable asociada (IntVar, StringVar).
- **command:** Función que se ejecuta cuando el valor cambia.
- **width:** Ancho del campo.

## Ejemplo básico (rango numérico)

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejemplo Spinbox (numérico)')

spin = tk.Spinbox(ventana, from_=0, to=10)
spin.pack(pady=10)

ventana.mainloop()
```

## Ejemplo avanzado con variable y valores personalizados

```python
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
```