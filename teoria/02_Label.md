# Label en Tkinter

El widget `Label` se utiliza para **mostrar texto o imágenes** en la ventana.
Es muy util para mostrar mensajes, titulos, o etiquetas para otros widgets.

## Sintaxis basica

```python
tk.Label(master, opciones)
```

- **master:** es la ventana o frame donde irá el Label.
- **opciones:** parámetros como text, fuente, color, tamaño, imagen, etc.

## Opciones más comunes

- **text:** Texto que se mostrará en el Label.
- **font:** Tipo y tamaño de letra. Ej: `('Arial', 14)`.
- **fg:** Color del texto.
- **bg:** Color de fondo.
- **image:** Muestra una imagen en el Label.
- **width / height:** Ancho y alto del Label en caracteres o pixeles.
- **anchor:** Alineación del texto `(n, s, e, w, center)`.
- **justify:** Justificación del texto `(left, center, right)`.
