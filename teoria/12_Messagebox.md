# Messagebox en Tkinter

El módulo `messagebox` de Tkinter permite mostrar **ventanas emergentes** con mensajes al usuario.
Se utilizan comúnmente para mostrar información, advertencias, errores o pedir confirmación.

## Importación

```python
from tkinter import messagebox
```

## Tipos de Messagebox más usados

- **`messagebox.showinfo(titulo, mensaje)`** Mensaje informativo.
- **`messagebox.showwarning(titulo, mensaje)`** Mensaje de advertencia.
- **`messagebox.showerror(titulo, mensaje)`** Mensaje de error.
- **`messagebox.askquestion(titulo, mensaje)`** Pregunta que devuelve 'yes' o 'no'.
- **`messagebox.askokcancel(titulo, mensaje)`** Pregunta que devuelve True o False.
- **`messagebox.askyesno(titulo, mensaje)`** Pregunta que devuelve True o False.
- **`messagebox.askretrycancel(titulo, mensaje)`** Devuelve True(Reintentar) o False(Cancelar).

## Ejemplo básico

```python
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title('Ejemplo Messagebox')

def mostrar_info()d:
    messagebox.showinfo('Información', 'Este es un mensaje informativo')

boton = tk.Button(ventana, text='Mostrar mensaje', command=mostrar_info)
boton.pack(pady=10)

ventana.mainloop()
```

## Ejemplo avanzado con confirmación

```python
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title('Messagebox avanzado')

def salir():
    respuesta = messagebox.askyesno('Confirmar salida', '¿Deseas salir?')
    if respuesta:
        ventana.destroy()

btn_info = tk.Button(ventana, text='Info')
btn_info.config(command=lambda: messagebox.showinfo('Info', 'Mensaje informativo'))
btn_info.pack(pady=10)

btn_error = tk.Button(ventana, text='Error')
btn_error.config(command=lambda: messagebox.showerror('Error', 'Ha ocurrido un error.'))
btn_error.pack(pady=10)

btn_salir = tk.Button(ventana, text='Salir', command=salir)
btn_salir.pack(pady=10)

ventana.mainloop()
```

