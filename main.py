# PRACTICA 2
# IPC2 - Javier Yllescas - 201906795

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

#paciente nuevo
crear_paciente("Juan Perez", 30, "Pediatria")
crear_paciente("Maria Mendez", 18, "Medicina General")

#EMULACION ATENCION
#Cada ciclo es un 1 minuto
minutosmax = 30
for minuto in range(1,minutosmax):
    print(f"\nMinuto {minuto}")
    
    #Atender paciente
    if persona_atendiendo != None:
        print(">> Atendiendo a:")
        persona_atendiendo.desplegar()
    else:
        persona_atendiendo = ColaPacientes.Pop()
        print("No hay pacientes en espera")
    