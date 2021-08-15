
from lista_enlazada_simple import listaSimpleEnlazada

def menu():
    opcion = ''
    estudiantes =  listaSimpleEnlazada()
    while opcion != '3':
        print('------------ Menu --------------')
        print('1. Ingresar estudiante')
        print('2. Ordenamiento Burbuja')
        print('4. Salir') 
        opcion = input('Ingrese una opción: ')
        print(opcion)
        if opcion == '1':
            carnet = input('Ingrese numero de carnet: ')
        
            estudiantes.crearEstudiante(carnet)
        elif opcion == '2':
            print('---------- Ordenamiento Burbuja ----------')
            estudiantes.metodoBurbuja1()
            estudiantes.mostrarEstudiantes()
            print('-------------------------------------------')
        else:
            break

menu() 







