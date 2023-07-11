import numpy as np
import os
import fundepa as fn
from gettext import npgettext



piso=np.empty([10,4], type(int))
os.system("cls")
fn.matriz(piso)

depa=0
op=0

while(op!=5):
    os.system("cls")
    print("             ¡Casa Feliz!            ")
    print("   ---------------------------------------")
    print("1.	Mostrar departamentos disponibles.")
    print("2.	Comprar departamento.")
    print("3.	Ver listado de compradores.")
    print("4.	Mostrar ganancia totales.")
    print("5.	Salir")
    
    op=fn.validar(op)
    if op==1:##opcion1
        fn.disponibles(piso)
        os.system("pause")

    if op==2:##opcion2
        depa=fn.validadepa
        comprueba=fn.buscar(piso, depa)
        if comprueba:     
            print("Este departamento está disponible.")
            pagar=fn.comprardepa(piso, depa)
            print("\t Total a pagar: $", pagar)
        else: 
            print("\t Departamento no disponible.")
        os.system("pause")

    if op==3:##opcion3
        depa=fn.validadepa(depa)
        listado=fn.mostarlista(piso, depa)
        os.system("pause")

    if op==4:##opcion4
        suma=0
        suma=fn.totalventa(piso)
        if (suma==0):
            print("\t No hay departamentos vendidos.")
        else:
            print("\t Total vendido: $ ", suma)
        os.system("pause")

    if op==5:##opcion5
        print("\tGracias por usar el servicio.")

