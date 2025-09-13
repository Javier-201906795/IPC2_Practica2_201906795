import os

def cola(ColaPacientes):
    print("\n" + "/"*10 + "Recorrer Cola" + "/"*10)
    numeropacientes = ColaPacientes.tamano() + 1
    paciente = None
    #Recorrer Cola
    for i in range(1,numeropacientes):
        if i <= 1:
            paciente = ColaPacientes.primero
        else:
            paciente = paciente.siguiente
        paciente.info.desplegar()
        #Datos
        nombre = paciente.info.nombre
        edad = paciente.info.edad   
        especialidadmedica = paciente.info.especialidadmedica
        minutoentredaatendido = paciente.info.minutoentredaatendido 
        print(f"Paciente: {nombre}, {edad}, {especialidadmedica}, {minutoentredaatendido}")

    print("\n" + "/"*10 + "Fin Recorrer Cola" + "/"*10)

def imagenCola(ColaPacientes):


    



        

    dot_text = """digraph ColaPacientes {
graph [rankdir=LR];
node [shape=box, style=filled, fillcolor=lightyellow, fontname="Helvetica"];
"""

#     dot_text += """
# paciente1 [label="Nombre: Maria Mendez\nEdad: 18\nEspecialidad Medica: Medicina General\nMinuto de entrada a cola: 17"];
# paciente2 [label="Nombre: Juan Perez\nEdad: 25\nEspecialidad Medica: Pediatría\nMinuto de entrada a cola: 20"];
# paciente3 [label="Nombre: Ana López\nEdad: 30\nEspecialidad Medica: Cardiología\nMinuto de entrada a cola: 23"];
# """

    print("\n" + "/"*10 + "Recorrer Cola" + "/"*10)
    numeropacientes = ColaPacientes.tamano() + 1
    paciente = None
    listanodos = ""
    #Recorrer Cola
    for i in range(1,numeropacientes):
        if i <= 1:
            paciente = ColaPacientes.primero
            listanodos += f"paciente{i} -> "
        elif i == numeropacientes -1:
            paciente = paciente.siguiente
            listanodos += f"paciente{i}"
        else:
            paciente = paciente.siguiente
            listanodos += f"paciente{i} -> "
        paciente.info.desplegar()
        #Datos
        nombre = paciente.info.nombre
        edad = paciente.info.edad   
        especialidadmedica = paciente.info.especialidadmedica
        minutoentredaatendido = paciente.info.minutoentredaatendido 
        print(f"Paciente: {nombre}, {edad}, {especialidadmedica}, {minutoentredaatendido}")
        dot_text += f'paciente{i} [label="Nombre: {nombre}\nEdad: {edad}\nEspecialidad Medica: {especialidadmedica}\nMinuto atendido: {minutoentredaatendido}"];\n'
        
    print("\n" + "/"*10 + "Fin Recorrer Cola" + "/"*10)



    dot_text += f"""
{listanodos};"""
    dot_text += "}"

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
