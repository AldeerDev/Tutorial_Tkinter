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

- **text** &#8594 Texto que se mostrará en el Label.
- **font** &#8594 Tipo y tamaño de letra. Ej: `('Arial', 14)`.
- **fg** &#8594 Color del texto.
- **bg** &#8594 Color de fondo.
- **image** &#8594 Muestra una imagen en el Label.
- **width / height** &#8594 Ancho y alto del Label en caracteres o pixeles.
- **anchor** &#8594 Alineación del texto `(n, s, e, w, center)`.
- **justify** &#8594 Justificación del texto `(left, center, right)`.
