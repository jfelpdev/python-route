# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:51:29 2020

@author: juanp
"""


def foreign_exchange_calculator(ammount):
      cop_to_usd = 0.00027 #Tipo de Cambio 6/07/2020
      return round(ammount / cop_to_usd)
def run():
    
    print("                                    UN")
    print("          UNIR  UNIR  UNIRUNIRUN  UNIR  UNIRUNIRU")
    print("           UNI   UNI   UNI   IRU   UNI  NIR   NIR")
    print("           RUN   RUN   RUN   UNI   RUN  UNIRUNIRU")
    print("           UNIRUNIRU   IRU   RUN   IRU  UNIR  UNIR")
    print("                                                IR")
    print()
    print('CALCULADORA DE DIVISAS')
    print('CONVIERTE PESOS COLOMBIANOS A DOLARES con EL CRACK PEDRAZA')
    print('')

    ammount = float(input('Ingrese la cantidad de dolares: '))
    result = foreign_exchange_calculator(ammount)
    print()

    print('${} dolares americanos son ${} pesos colombianos'.format(ammount,result))

if __name__ == '__main__': 
    run()