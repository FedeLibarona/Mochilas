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
continuar = Y,N
comenzar = "Y"

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
     comenzar = input("¿ Comenzar/Seguir?")   
     if comenzar == "Y":
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
                print("Pone marca valida")
             else:
                print ("Genial")
                break
             continue

     
          while True:
               if marcas == "JHON FOOS" and marcas == "WILSON":
                  cuentamarca+=1
                  print(cuentamarca)
                  break
              
  
          while True:    
            if tamano >0 or tamano <9:
             cuentatamano+=1
             print(cuentatamano)
            break
          continue
     else:
      print("Gracias")
      break 
  
 
        
           
    
        
        

        
    
        
        
        
    
          