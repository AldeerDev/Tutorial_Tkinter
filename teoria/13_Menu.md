# Menú en Tkinter

El widget `Menu` permite crear **barras de menú** en la parte superior de la ventana y menús desplegables.

## Creacion básica

1. Se crea la barra de menús principal.
2. Se añaden menús desplegables (Archivo, Editar, etc.).
3. Se agregar comandos a cada menú.

## Sintaxis

```python
menu = tk.Menu(ventana)
ventana.config(menu=menu)
```

## Opciones comunes

- **`add_command(label='Texto', command=función)`** Agrega una opción al menú.
- **`add_separator()`** Agrega una línea separadora.
- **`add_cascade(label='Texto', menu=submenu)`** Agrega un submenú.
- **`tearoff=0`** Quita la línea punteada que permite 'separar' el menú (se recomienda usarlo).