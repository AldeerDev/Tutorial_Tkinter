# Frame en Tkinter

El widget `Frame` es un **contenedor** que se utiliza para agrupar otros widgets.
Es muy util para organizar la interfaz en secciones o paneles.

## Sintaxis básica

```python
tk.Frame(master, opciones)
```

- **master:** ventana o contenedor donde se coloca el Frame.
- **opciones:** parámetros como color, borde, tamaño, atc.

## Opciones más comunes

- **bg:** Color de fondo del Frame.
- **bd:** Ancho del borde en píxeles.
- **relief:** Estilo del borde:
  - "flat" (plano, por defecto).
  - "raised" (elevado).
  - "sunken" (hundido).
  - "groove" (surco).
  - "ridge" (bisel).
- **width / height:** Tamaño del Frame (solo si no se ajusta el contenido).

## Ejemplo básico

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejemplo Frame')

frame = tk.Frame(ventana, bg='lightblue', bd=2, relief='sunken')
frame.pack(padx=20, pady=20)

tk.Label(frame, text='Soy un Label dentro del Frame').pack(pady=5)
tk.Button(frame, text='Soy un Button dentro del Frame').pack(pady=5)

ventana.mainloop()
```
