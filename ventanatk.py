import tkinter as tk

from funciones import *


ventana = tk.Tk()
ventana.geometry("1000x600")
ventana.title("Practica 2 - IPC2 ")

etiqueta = tk.Label(ventana, text="FIFO - Cola de Pacientes", font=("Arial", 16))
etiqueta.pack(pady=10)

# Frame para los campos de entrada
frame_campos = tk.Frame(ventana)
frame_campos.pack(pady=20)

# Nombre
tk.Label(frame_campos, text="Nombre:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entrada_nombre = tk.Entry(frame_campos, width=30)
entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

# Edad
tk.Label(frame_campos, text="Edad:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entrada_edad = tk.Entry(frame_campos, width=30)
entrada_edad.grid(row=1, column=1, padx=5, pady=5)

# Especialidad Médica
tk.Label(frame_campos, text="Especialidad Medica:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entrada_especialidad = tk.Entry(frame_campos, width=30)
entrada_especialidad.grid(row=2, column=1, padx=5, pady=5)

# Botón para agregar paciente
def agregar_paciente():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    especialidad = entrada_especialidad.get()
    print(f"Nombre: {nombre}, Edad: {edad}, Especialidad Médica: {especialidad}")

boton_agregar = tk.Button(ventana, text="Agregar Paciente", command=agregar_paciente)
boton_agregar.pack(pady=20)


ventana.mainloop()