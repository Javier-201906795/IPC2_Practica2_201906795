# PRACTICA 2
# IPC2 - Javier Yllescas - 201906795

from Nodos import *



#Crear un paciente
paciente = Paciente("Mario Lopez", 30, "Medicina General")
paciente.desplegar()


#Variables
ColaPacientes = Cola()
persona_atendiendo = None

#Cada ciclo es un 1 minuto
minutosmax = 30
for minuto in range(1,minutosmax):
    print(f"\nMinuto {minuto}")