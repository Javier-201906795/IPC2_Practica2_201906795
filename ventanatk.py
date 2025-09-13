import tkinter as tk

from funciones import *



#Variables
contador_tiempo = 0
tiempofalante = 0

persona_atendiendo = None


def mostrar_paciente():
    if persona_atendiendo == None:
        label_paciente.config(text="No hay paciente siendo atendido")
    else:
        nombre = persona_atendiendo.nombre
        edad = persona_atendiendo.edad
        especialidad = persona_atendiendo.especialidadmedica
        
        # Aquí puedes calcular minutos de entrada y atendido, por ahora pongo valores de ejemplo
        minuto_entrada = persona_atendiendo.minutoentradaalacola
        minuto_atendido = persona_atendiendo.minutoentredaatendido
        
        texto = f"Nombre: {nombre}\nEdad: {edad}\nEspecialidad Medica: {especialidad}\nMinuto de entrada a Cola: {minuto_entrada}\nMinuto atendido: {minuto_atendido}"
        label_paciente.config(text=texto)


def atender_paciente(minuto):
    global persona_atendiendo
    global tiempofalante
    #Atender paciente
    if persona_atendiendo != None:
        print(">> Atendiendo a:")
        
        persona_atendiendo.desplegar()
        tiempofalante = tiempo_faltante(persona_atendiendo, minuto)
        print(f"------------------------------------> Tiempo faltante: {tiempofalante} minutos")
        label_tiempofaltante.config(text=f"Tiempo Faltante: {tiempofalante}")

        if tiempofalante <= 0:
            print(">>> Paciente atendido")
            persona_atendiendo = None
        
    else:
        #Guardar tiempo paciente atendido
        guardar_tiempo_atencion(minuto)
        #Agregar paciente a atender
        persona_atendiendo = ColaPacientes.Pop()
        if persona_atendiendo != None:
            print(">>> Nuevo paciente a atender:")
            persona_atendiendo.asignarminutoentredaatendido(minuto)
            persona_atendiendo.desplegar()
    #Muestra en un texto la informacion del paciente
    mostrar_paciente()
    #Graficar cola
    graficar_cola()












ventana = tk.Tk()
ventana.geometry("1000x650")
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
    #Funciones
    crear_paciente(nombre, edad, especialidad, contador_tiempo)
    #Limpiar campos
    entrada_nombre.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    entrada_especialidad.delete(0, tk.END)
    #Graficar cola
    graficar_cola()


boton_agregar = tk.Button(ventana, text="Agregar Paciente", command=agregar_paciente)
boton_agregar.pack(pady=20)


#Abrir imagen cola
def abrir_cola():
    import os
    os.startfile("Cola.png")
    


boton_imagen = tk.Button(ventana, text="Abrir Cola", command=abrir_cola)
boton_imagen.pack(pady=20)





# Label de tiempo
label_tiempo = tk.Label(ventana, text="Tiempo: 0", font=("Arial", 20, "bold"), fg="blue")
label_tiempo.pack(pady=10)



# Función para incrementar el tiempo
def incrementar_tiempo1():
    global contador_tiempo
    contador_tiempo += 1
    label_tiempo.config(text=f"Tiempo: {contador_tiempo}")
    atender_paciente(contador_tiempo)

def incrementar_tiempo5():
    global contador_tiempo
    contador_tiempo += 5
    label_tiempo.config(text=f"Tiempo: {contador_tiempo}")
    atender_paciente(contador_tiempo)

def incrementar_tiempo10():
    global contador_tiempo
    contador_tiempo += 10
    label_tiempo.config(text=f"Tiempo: {contador_tiempo}")
    atender_paciente(contador_tiempo)

# Frame para contener los botones de tiempo
frame_botones_tiempo = tk.Frame(ventana)
frame_botones_tiempo.pack(pady=10)

# Botones Timpo
boton_tiempo1 = tk.Button(frame_botones_tiempo, text="Incrementar Tiempo + 1", command=incrementar_tiempo1)
boton_tiempo1.pack(side="left", padx=5)

boton_tiempo5 = tk.Button(frame_botones_tiempo, text="Incrementar Tiempo + 5", command=incrementar_tiempo5)
boton_tiempo5.pack(side="left", padx=5)

boton_tiempo10 = tk.Button(frame_botones_tiempo, text="Incrementar Tiempo + 10", command=incrementar_tiempo10)
boton_tiempo10.pack(side="left", padx=5)


# Botón 
boton_mostrar = tk.Button(ventana, text="Mostrar Paciente", command=mostrar_paciente)
boton_mostrar.pack(pady=5)


# Label de tiempo
label_tiempofaltante = tk.Label(ventana, text="Tiempo Faltante: 0", font=("Arial", 20, "bold"), fg="blue")
label_tiempofaltante.pack(pady=5)

# Label para mostrar los datos del paciente
label_paciente = tk.Label(ventana, text="", font=("Arial", 12), justify="left")
label_paciente.pack(pady=10)







ventana.mainloop()