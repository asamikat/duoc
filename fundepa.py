import numpy as np
import os

def matriz(mat):
    p=1
    for i in range(10):
        for j in range(4):
            mat[i,j]=p
            p+=1
            
def validar(op):
    while(True):
        try:
            op=int(input("Elija opción: "))
            if op>=1 and op<=5:
                break
            else:
                print("Debe ingresar opción entre 1 a 5")
        except ValueError:
            print("Debe ser un número entero")
    return op

def disponibles(piso):
    os.system("cls")
    for i in range(10):
        print("\n") 
        for j in range(4):
            if(j==1):
                print("\t",piso[i,j], end="  ")
            else:
                print("\t",piso[i,j], end="  ")

    
def validadepa(depa):
   depa=0
   while True:
        try: 
            depa=int(input("Ingrese número de departamento: "))
            if depa>=1 and depa<=40:
                break
            else:
                print(" Ingrese departamento entre 1 y 40")
        except ValueError:
            print(" Ingrese departamento entre  1 y 40")
   return depa

def buscar(piso, depa):
    for h in range(10):
        for i in range(4):
            if depa==piso[h,i]:
                return True
    return False
 
def comprardepa(piso, depa):
    for b in range(10):
        for i in range(4):
            if piso[b,i]==piso:
                piso[b,i]=0          
                if i==0 or i==3:
                    pago=3800
                if i==1 or i==2:
                    pago=3000
    return pago

def mostarlista(piso, depa):
    print#elprintessoloporquesinosecaeelsistema
    
def totalventa(piso):
    sum=0
    for a in range(10):
        for i in range(4):
            if piso[a,i]==0:
                if i==0 or i==3:
                    sum+=0
                if i==1 or i==2:
                    sum+=0
    return sum