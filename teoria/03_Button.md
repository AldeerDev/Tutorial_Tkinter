# Button en Tkinter

El widget `Button` se utiliza para **ejecutar una acción** cuando el usuario hace clic sobre él.
Normalmente se lo asocia a una **función** mediante el parámetro `command`.

## Sintaxis básica

```python
tk.Button(master, opciones)
```

- **master:** ventana o contenedor donde irá el botón.
- **opciones:** parámetros como texto , colores, comando, etc.

## Opciones más comunes

- **text:** Texto que muestra el botón.
- **command:** Función a ejecutar al hacer clic.
- **font:** Tipo y tamaño de letra.
- **fg:** Color del texto.
- **bg:** Color de fondo.
- **widht / height:** Ancho y alto del botón.
- **state:** Estado del botón:
  - "normal" (activo).
  - "disabled" (deshabilitado).
  - "active" (cuando se presiona).
- **image:** Mostrar una imagen en el botón.

## Ejemplo básico

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejemplo de Button')

def saludar():
    print('¡Hola desde el botón!')

boton = tk.Button(ventana, text='Saludar', command=saludar)
boton.pack(pady=20)

ventana.mainloop()
```
