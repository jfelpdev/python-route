# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:43:09 2020

@author: juanp
"""


def foreign_exchange_calculator(ammount, convertir):
    bitcoin_usd = 7200
    bitcoin_cop = 24000000
    bitcoin_mxn = 135000

    if(convertir == 1):
        return ammount / bitcoin_usd
    elif(convertir == 2):
        return ammount / bitcoin_cop
    elif(convertir == 3):
        return ammount / bitcoin_mxn


def run():
    print("=============================================")
    print("=                   ==  ==                  =")
    print("=                   ==  ==                  =")
    print("=                ==========                 =")
    print("=                 ==       ==               =")
    print("=                 ==       ==               =")
    print("=                 ==========                =")
    print("=                 ==       ==               =")
    print("=                 ==       ==               =")
    print("=                ===========                =")
    print("=                   ==  ==                  =")
    print("=                   ==  ==                  =")
    print("=          N A S H  E X C H A N G E         =")
    print("= C A L C U L A D O R A  D E  B I T C O I N =")
    print("=============================================")
    print("Convierte Tu moneda local a BITCOIN .")
    print("")
    print("De Dolares          : USD a BTC : Presiona 1 ")
    print("De Pesos Colombianos: COP a BTC : presiona 2 ")
    print("De Pesos Mexicanos  : MXN a BTC : presiona 3 ")
    print("")

    option1 = int(input("¿Que tipo de cambio deseas? "))

    if(option1 == 1):
        ammount = int(input("¿Cuantos USD deseas cambiar a BTC? : "))
        result = float(foreign_exchange_calculator(ammount, option1))
        print("${} USD Dolares son {} BTC".format(ammount, (round(result, 8))))
        print("")

    elif(option1 == 2):
        ammount = int(input("Cuantos COP deseas cambiar a BTC? : "))
        result = float(foreign_exchange_calculator(ammount, option1))
        print("${} COP Pesos Colombianos son {} BTC".format(ammount, (round(result, 8))))
        print("")

    elif(option1 == 3):
        ammount = int(input("Cuantos MXN deseas cambiar a BTC? : "))
        result = float(foreign_exchange_calculator(ammount, option1))
        print("${} MXN Pesos Mexicanos son {} BTC".format(ammount, (round(result, 8))))
        print("")

if __name__ == "__main__":
    run()
    print("Gracias por su Visita")
    print("Recuerda : TODOS SOMOS SATOSHI :)")