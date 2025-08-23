# Listbox en Tkinter

El widget `Listbox` permite mostrar una lista de elementos en forma vertical.
El usuario puede **seleccionar uno o varios items** de la lista.

## Sintaxis básica

```python
tk.Listbox(master, opciones)
```

- **master:** ventana o contenedor donde se coloca el Listbox.
- **opciones:** parámetros como alto, ancho, modo de selección, etc.

## Opciones más comunes

- **height:** Número de elementos visibles (si hay más, aparece scroll).
- **width:** Ancho en caracteres.
- **fg:** Color del texto.
- **bg:** Color de fondo.
- **font:** Tipo y tamaño de letra.
- **selectmode:** Modo de selección:
  - "browse" (uno a la vez, por defecto).
  - "single" (igual que browse pero con limitaciones).
  - "multiple" (varios, sin necesidad de Ctrl).
  - "extended" (varios con Ctrl o Shift).

## Métodos importantes

- **.insert(indice, elemento)** Insertar un elemento en la lista.
  - tk.END Añade al final.
- **.delete(inicio, fin)** Elimina elemento por indice.
- **.get(inicio, fin)** Obtiene elementos.
- **.curselection()** Devuelve los indices seleccionados.

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejemplo Listbox')

lista = tk.Listbox(ventana)
lista.pack()

# Agregar elementos
for item in ['Pyhton', 'Java', 'C++', 'JavaScript']:
    lista.insert(tk.END, item)

def mostrar():
    seleccion = lista.curselection()
    if seleccion:
        print('Seleccionado: ', lista.get(seleccion[0]))

boton = tk.Button(ventana, text='Mostrar seleccion', command=mostrar)
boton.pack()

ventana.mainloop()
```
