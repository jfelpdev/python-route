# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:21:27 2020

@author: juanp
"""

#def imprimir_mensaje(): #esto es un bloque de codigo 
   ##print("¡Estoy aprendiendo a usar funciones!")
    
#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()



def conversacion(mensaje):
    print("Hola")
    print("Cómo estas?")
    print(mensaje)
    print("Adios")

opcion = int(input("Elige una opción(1, 2, 3): "))

if opcion == 1:
    conversacion("Elegiste la opción 1")
    
elif opcion == 2:
    conversacion("Elegiste la opción 2")
    
elif opcion == 3:
    conversacion("Elegiste la opción 3")   
    
else: 
    print("Escribe la opción correcta")