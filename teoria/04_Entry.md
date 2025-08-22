# Entry en Tkinter

El widget `Entry` se utiliza para el usuario pueda **ingresar texto de una sola linea**.
Se usa comúnmente  en formularios (usuario, contraseña, correo, etc.).

## Sintaxis básica

```python
tk.Entry(master, opciones)
```

- **master:** ventana o contenedor donde irá el Entry.
- **opciones:** parámetros como ancho, texto inicial, modo de entrada, etc.

## Opciones más comunes

- **width:** Ancho del campo (en caracteres).
- **show:** Caracter que se muestra en lugar del texto (util para contraseñas).
- **fg:** Color de texto.
- **bg:** Color de fondo.
- **state:** Estado del campo:
  - "normal".
  - "disabled".
  - "readonly".
- **textvariable:** Vincular el contenido con una variable `tk.StringVar`.

## Métodos importantes

- **.get()** Obtiene el texto escrito en el Entry.
- **.delete(inicio, fin)** Borra texto desde la posición `inicio` hasta `fin`.
  - 0 = primera posición.
  - `tk.END` = hasta el final.
- **.insert(indice, texto)** Inserta texto en una posición específica.

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejemplo Entry')

entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

def mostrar_texto():
    print('Texto ingresado:', entrada.get())

boton = tk.Button(ventana, text='Mostrar', command=mostrar_texto)
boton.pack()

ventana.mainloop()
```
