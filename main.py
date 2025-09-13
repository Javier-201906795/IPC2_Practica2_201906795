# PRACTICA 2
# IPC2 - Javier Yllescas - 201906795

import os
from Nodos import *




#Variables
ColaPacientes = Cola()
persona_atendiendo = None



def crear_paciente(nombre,edad, especialidad):
    print( "\n************* [ Nueovo Paciente ] ***********")
    #Crear un paciente
    paciente = Paciente(nombre, edad, especialidad)
    paciente.desplegar()
    print("*********************************************")
    #Agregar a la cola
    print("------------------ [Cola] ----------------------")
    ColaPacientes.Push(paciente)
    ColaPacientes.desplegar()
    print("-- [FINCola] -----------------------------------")


def tiempo_faltante(paciente, minuto_actual):
    especialidad = paciente.especialidadmedica
    tiempoentrada = paciente.minutoentredaatendido
    tiempoestimado = 0

    if especialidad == "Medicina General":
        tiempoestimado = 10
    elif especialidad == "Pediatria":
        tiempoestimado = 15
    elif especialidad == "Ginecologia":
        tiempoestimado = 20
    elif especialidad == "Dermatologia":
        tiempoestimado = 25
    
    return tiempoestimado - (minuto_actual - tiempoentrada)


def imagenCola():
        

    dot_text = """digraph ColaPacientes {
graph [rankdir=LR];
node [shape=box, style=filled, fillcolor=lightyellow, fontname="Helvetica"];

paciente1 [label="Nombre: Maria Mendez\nEdad: 18\nEspecialidad Medica: Medicina General\nMinuto de entrada a cola: 17"];
paciente2 [label="Nombre: Juan Perez\nEdad: 25\nEspecialidad Medica: Pediatría\nMinuto de entrada a cola: 20"];
paciente3 [label="Nombre: Ana López\nEdad: 30\nEspecialidad Medica: Cardiología\nMinuto de entrada a cola: 23"];

paciente1 -> paciente2 -> paciente3;
}
"""

    

    # Guardar el archivo .dot
    with open("1_Grafica.dot", "w", encoding="utf-8") as f:
        f.write(dot_text)

    print(">> Archivo 1_Grafica.dot generado")

    #Crear Imagen
    try:
        os.system(f"dot -Tpng 1_Grafica.dot -o Cola.png")
        print(f">>Imagen Cola.png generada")
    except:
        print("!! Error al crear imagen ¡¡¡")







#paciente nuevo
crear_paciente("Juan Perez", 30, "Pediatria")
crear_paciente("Maria Mendez", 18, "Medicina General")

#EMULACION ATENCION
#Cada ciclo es un 1 minuto
minutosmax = 35
for minuto in range(1,minutosmax):
    print(f"\nMinuto {minuto}")
    
    #Atender paciente
    if persona_atendiendo != None:
        print(">> Atendiendo a:")
        
        persona_atendiendo.desplegar()
        tiempofalante = tiempo_faltante(persona_atendiendo, minuto)
        print(f"------------------------------------> Tiempo faltante: {tiempofalante} minutos")

        if tiempofalante <= 0:
            print(">>> Paciente atendido")
            persona_atendiendo = None
        
    else:
        #Agregar paciente a atender
        persona_atendiendo = ColaPacientes.Pop()
        if persona_atendiendo != None:
            print(">>> Nuevo paciente a atender:")
            persona_atendiendo.asignarminutoentredaatendido(minuto)
            persona_atendiendo.desplegar()
        
    
#Crear imagen de la cola
imagenCola()
