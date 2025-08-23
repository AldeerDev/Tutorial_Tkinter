# Text en Tkinter

El widget `Text` permite al usuario **ingresar y mostrar texto de varias líneas**.
Se utiliza en editores, campos de comentarios o cualquier lugar donde se necesite texto extenso.

## Sintaxis básica

```python
tk.Text(master, opciones)
```

- **master:** ventana o contenedor donde coloca el text.
- **opciones:** parámetros como tamaño, fuente, colores, etc.

## Opciones más comunes

- **width:** Ancho de caracteres.
- **height:** Alto de lineas.
- **font:** Tipo y tamaño de letra.
- **fg:** Color de texto.
- **bg:** Color de fondo.
- **wrap:** Controla el ajuste de línea:
  - "char" ajusta por caracteres.
  - "word" ajusta por palabras.
  - "none" sin ajuste (aparece scroll).
- **state:** Estado del widget:
  - "nomal".
  - "disabled".

## Métodos importantes

- **.get(inicio, fin)** Obtiene el texto entre las posiciones dadas.
  - "1.0" Linea 1, carácter 0 (incio).
  - tk.END Hasta el final.
- **.insert(indice, texto)** Insertar texto en una posición.
- **.delete(inicio, fin)** Elimina texto entre posiciones.

## Ejemplo básico

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejemplo Text')

caja_texto = tk.Text(ventana, width=40, height=10)
caja_texto.pack(pady=10)

def mostrar():
    contenido = caja_texto.get('1.0', tk.END) # Desde la línea 1, caracter 0 hasta el final.
    print('Texto ingresado:\n', contenido)

boton = tk.Button(ventana, text='Mostrar contenido', command=mostrar)
boton.pack()

ventana.mainloop()
```
