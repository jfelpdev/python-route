# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:43:23 2020

@author: juanp
"""
def foring_change_calculator(ammount):
    mex_to_col_rate = 145.97
    
    return mex_to_col_rate*ammount
    
    
def run():
    print("CALCULADORA DE DIVISAS")
    print("CONVIERTE PESOS MEXICANOS A PESOS COLOMBIANOS")
    print()
    
    ammount = float(input("Ingresa la cantidad de pesos mexicanos que quieras convertir a pesos colombianos"))
    
   result = foreing_exchange_calculator(ammount)
   print("${} pesos mexicanos son ${} pesos colombianos.".format(ammount, result))
   print()
if _name_=="_main_":
    run()


