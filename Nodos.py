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
    

class ListaSimple:

    def __init__(self):
        self.primero = None
        self.longitud = 0
    
    def obtenerprimero(self):
        return self.primero

    def estaVacia(self):
        return self.primero == None

    def agregar(self,item):
        nuevo = Nodo(item)
        nuevo.asignarSiguiente(self.primero)
        self.primero = nuevo
        self.longitud += 1

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
            actual.obtenerDato().desplegar()
            actual = actual.obtenerSiguiente()

    def buscar(self,item):
        actual = self.primero
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato().EsIgualALLave(item):
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()

        return encontrado

    def eliminar(self,item):
        actual = self.primero
        previo = None
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato().EsIgualALLave(item):
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        if previo == None:
            if self.primero != None:
                self.primero = actual.obtenerSiguiente()
                print("Eliminado1")
        else:
            if encontrado:
                previo.asignarSiguiente(actual.obtenerSiguiente())
                print("Eliminado2")
            else:
                print("no encontrado")

    def obtener(self, indice):
        if indice < 0 or indice >= self.longitud:
            return None
        actual = self.primero
        for i in range(indice):
            actual = actual.siguiente
        return actual.valor
    
    def buscar_indice(self, id_buscar):
        # Busca el índice de un elemento por su id
        actual = self.primero
        indice = 0
        while actual:
            #Valida si existe el valor id y si si el id es igual
            if hasattr(actual.valor, 'id') and actual.valor.id == id_buscar:
                return indice
            actual = actual.siguiente
            indice += 1
        return -1
    

class Paciente(InfoNodo):
    def __init__(self, nombre, edad, especialidadmedica):
        self.nombre = nombre
        self.edad = edad
        self.especialidadmedica = especialidadmedica
        self.id = None
        self.minutoentredaacola = None
    
    def asignarminutoentredaacola(self, minuto):
        self.minutoentredaacola = minuto

    def asignarid(self, id):
        self.id = id

    def EsIgualALLave(self, id):
        return self.id == id

    def desplegar(self):
        print("\n-------------------")
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Especialidad Medica: ", self.especialidadmedica)
        print("ID: ", self.id)
        print("Minuto de entrada a cola: ", self.minutoentredaacola)
        print("-------------------\n")