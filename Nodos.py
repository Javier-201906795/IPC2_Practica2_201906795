class InfoNodo():
    
    def desplegar():
        pass
    
    def EsIgualALLave():
        pass

class Nodo:
    def __init__(self,info):
        self.info = info
        self.siguiente = None

    def obtenerInfo(self):
        return self.info

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarInfo(self,info):
        self.info = info

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

class Cola:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def estaVacia(self):
        return self.primero == None

    def Push(self,item):
        nuevo = Nodo(item)
        
        if self.primero != None: 
            self.ultimo.asignarSiguiente(nuevo)
        else:
            self.primero = nuevo
            
        self.ultimo = nuevo
            
    def tamano(self):
        actual = self.primero
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
        return contador

    def desplegar(self):
        actual = self.primero
        while actual != None:
            actual.obtenerInfo().desplegar()
            actual = actual.obtenerSiguiente()

    def buscar(self,item):
        actual = self.primero
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerInfo().EsIgualALLave(item):
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()

        return encontrado

    def Pop(self):
        primerotemp = self.primero
        if self.primero != None:
            self.primero.obtenerInfo().desplegar()                    
            self.primero = self.primero.obtenerSiguiente()
        else:
            print("Cola esta vacia")
            return None
            
        return primerotemp.obtenerInfo()
    


class Paciente(InfoNodo):
    def __init__(self, nombre, edad, especialidadmedica):
        self.nombre = nombre
        self.edad = edad
        self.especialidadmedica = especialidadmedica
        self.minutoentredaatendido = None
    
    def asignarminutoentredaatendido(self, minuto):
        self.minutoentredaatendido = minuto

    def desplegar(self):
        print("\n-------------------")
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Especialidad Medica: ", self.especialidadmedica)
        print("Minuto de entrada a cola: ", self.minutoentredaatendido)
        print("-------------------\n")