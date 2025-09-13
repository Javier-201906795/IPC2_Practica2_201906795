# PRACTICA 2
# IPC2 - Javier Yllescas - 201906795

import os
from Nodos import *
from graficagraphviz import imagenCola, cola




# #Variables
ColaPacientes = Cola()
# persona_atendiendo = None



def crear_paciente(nombre,edad, especialidad, tiempoentrada):
    print( "\n************* [ Nueovo Paciente ] ***********")
    #Crear un paciente
    paciente = Paciente(nombre, edad, especialidad, tiempoentrada)
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
    tiempoestimado = 1

    if especialidad == "Medicina General":
        tiempoestimado = 10
    elif especialidad == "Pediatria":
        tiempoestimado = 15
    elif especialidad == "Ginecologia":
        tiempoestimado = 20
    elif especialidad == "Dermatologia":
        tiempoestimado = 25
    
    return tiempoestimado - (minuto_actual - tiempoentrada)






# #paciente nuevo
# crear_paciente("Juan Perez", 30, "Pediatria",1)
# crear_paciente("Maria Mendez", 18, "Medicina General",5)
# crear_paciente("Juan Perez", 30, "Pediatria",1)
# crear_paciente("Juan Perez", 30, "Pediatria",1)
# crear_paciente("Juan Perez", 30, "Pediatria",1)
# crear_paciente("Juan Perez", 30, "Pediatria",1)
# crear_paciente("Juan Perez", 30, "Pediatria",1)


# #Crear imagen de la cola
# imagenCola(ColaPacientes)
# print("/"*10 + "Cola" + "/"*10)
# cola(ColaPacientes)



# #EMULACION ATENCION
# #Cada ciclo es un 1 minuto
# minutosmax = 35
# for minuto in range(1,minutosmax):
#     print(f"\nMinuto {minuto}")
    
#     #Atender paciente
#     if persona_atendiendo != None:
#         print(">> Atendiendo a:")
        
#         persona_atendiendo.desplegar()
#         tiempofalante = tiempo_faltante(persona_atendiendo, minuto)
#         print(f"------------------------------------> Tiempo faltante: {tiempofalante} minutos")

#         if tiempofalante <= 0:
#             print(">>> Paciente atendido")
#             persona_atendiendo = None
        
#     else:
#         #Agregar paciente a atender
#         persona_atendiendo = ColaPacientes.Pop()
#         if persona_atendiendo != None:
#             print(">>> Nuevo paciente a atender:")
#             persona_atendiendo.asignarminutoentredaatendido(minuto)
#             persona_atendiendo.desplegar()
        
    

