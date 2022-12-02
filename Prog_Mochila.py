#############################################
# Primer commit main App-Prueba
# *Subir a Gitthub
# * Index.py
# ejecutable.exe
# release :   19/09/2022
# developer : Federico Libarona

#############################################

from ast import While
from operator import concat
from tkinter import N, Y
import math
import openpyxl


#main-resources
continuamos = N, Y

marcas = "JHON FOOS", "WILSON" 

tamano = 1, 2, 3, 4, 5, 6, 7, 8


cuentamarca = 0
cuentatamano = 0
cuentamarcatotal  =  cuentamarca
cuentatamanototal =  cuentatamano

#index
#marca = input ("ingrese marca")
#print ("usted quiere, " + marca)

#tamano = input("ingrese tamano")
#print ("usted quiere, " + tamano)
 
    
    
    
while True:
        tamano = int(input("ingrese tamano"))
        if tamano > 8 or tamano == 0 :
              print("Pone un tamano valido")
        else: 
              print("Genial")
              break
        continue

while True:
        marcas =(input("ingresemarcas"))
        if marcas != "JHON FOOS" and marcas != "WILSON":
         print("Pone marcas")
        else:
            print ("Genial")
            break
        continue
    
    
    
    #definimos la forma de importacion
wb = openpyxl.load_workbook ( "C:\Desarrollo\Git\clientes.xlsx")

ws = wb ["clientes"]

print ("wb.sheetname")

 #fecha entrega 
 

 #cambio en la variables (contador)#variable de contador 
    
 #clase que cuenta de forma generica e imprime en consola
 
 



     #calendario-utilidad en calendario.py


     #cambios en las variables (CONTADOR)
     #CLASE QUE CUENTA DE FORMA GENERICA E IMPRIME EN CONSOLA
     
while True:
        if marcas == "JHON FOOS" and marcas == "WILSON":
         cuentamarca+=1
         print(cuentamarca)
         break
        continue
while True:    
        if tamano >0 or tamano <9:
         cuentatamano+=1
         print(cuentatamano)
        break

while True:
        continuamos = print("¿Quiere continuar?")
        if continuamos != N:
          print("muchas gracias")
          break
     
           
    
        
        

        
    
        
        
        
    
          