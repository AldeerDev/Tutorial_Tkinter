# Ventana Principal en Tkinter

La ventana principal es el **contenedor base** de cualquier aplicacion en Tkinter.
Se crea con el objeto `Tk()`.

## Se crea una ventana basica

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title('Mi primer ventana')
ventana.geometry('400x300')
ventana.mainloop()
```

## Explicacion de cada linea

1. import tkinter as tk -> importa la libreria tkinter.
2. ventana = tk.Tk() -> crea la ventana principal.
3. ventana.title -> Titulo de la ventana.
4. ventana.geometry() -> define el tamaño inicial (ancho x alto).
5. ventana.mainloop() -> Mantiene la ventana abierta hasta que el usuario la cierre.
