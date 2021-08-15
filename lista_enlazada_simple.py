from nodo import Nodo


class listaSimpleEnlazada():
    def __init__(self):
        self.primero = None
        self.ultimo = None


    #MEtodo que verifica si la lista esta vacia o llena

    def crearEstudiante(self, carnet):  #insertar a final
        nuevo = Nodo(carnet) #nuevo estudiante
       
        if self.primero is None:
            self.primero = nuevo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo


    def eliminarUltimo(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente
        print(aux.siguiente.carnet)
        aux.siguiente = None
        self.ultimo = aux


    def metodoBurbuja1(self):
        comprobar = self.primero 
        aux = self.primero 
        if comprobar.siguiente != None and aux != None:
            i = self.primero
            while i != None:
                j = i.siguiente
                while j != None:
                    if i.carnet > j.carnet:
                        temporal = i.carnet
                        i.carnet = j.carnet
                        j.carnet = temporal
                    j = j.siguiente
                i = i.siguiente
        else: 
            print("")    

    def mostrarEstudiantes(self):
        tmp = self.primero
        while tmp is not None:
            print(f'Carnet :{tmp.carnet}')
            tmp = tmp.siguiente
