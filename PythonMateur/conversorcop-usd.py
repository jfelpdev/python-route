# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 08:41:59 2020

@author: juanp
"""

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos" + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")
    

menu = """
                                     UN
        UNIR  UNIR  UNIRUNIRUN  UNIR  UNIRUNIRU
         UNI   UNI   UNI   IRU   UNI  NIR   NIR
         RUN   RUN   RUN   UNI   RUN  UNIRUNIRU
         UNIRUNIRU   IRU   RUN   IRU  UNIR  UNIR
                                              IR

Bienvenido al conversor de monedas 🤑🤑

1 - Pesos Colombianos (COP)
2 - Pesos Mexicanos (MX)
3 - Pesos Argentinos (ARGTS)

Elige una opción: """

opcion = input(menu)


if opcion == "1":
    conversor("colombianos", 3631)
    
elif opcion == "2":
    conversor("mexicanos", 22.70)
    
elif opcion == "3":
    pesos = input("argentinos", 70.87)

else:
    print("ingresa una opción correcta por favor.")