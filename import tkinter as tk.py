
import tkinter as tk
from tkinter import messagebox

# Función para determinar si el año es bisiesto
def verificar_bisiesto():
    try:
        # Obtener el año ingresado por el usuario
        año = int(entry_año.get())
        
        # Verificar si el año es bisiesto
        if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
            messagebox.showinfo("Resultado", f"El año {año} es un año bisiesto.")
        else:
            messagebox.showinfo("Resultado", f"El año {año} NO es un año bisiesto.")
    
    except ValueError:
        # Si el usuario ingresa algo que no es un número
        messagebox.showerror("Error", "Por favor ingrese un número válido para el año.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Verificador de Año Bisiesto")

# Etiqueta de instrucciones
etiqueta = tk.Label(ventana, text="Ingrese un año para verificar si es bisiesto:")
etiqueta.pack(pady=10)

# Campo de texto para ingresar el año
entry_año = tk.Entry(ventana, width=20)
entry_año.pack(pady=5)

# Botón para verificar si el año es bisiesto
boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_bisiesto)
boton_verificar.pack(pady=10)

# Ejecutar el bucle de la ventana
ventana.mainloop()
