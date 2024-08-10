import os
def menu():
    print("----------------------------------")
    print("========== Calculadora ===========")
    print("------------ 1 - Soma ------------")
    print("---------- 2 - Subtração ---------")
    print("----------- 3 - Divisão ----------")
    print("------ 4 - Multiplicação ---------")
    print("------------ 5 - Sair ------------")
    print("----------------------------------")

def soma(numero1=None, numero2=None):
    resultado = numero1 + numero2
    print(numero1, " + ", numero2, " = ", resultado)
    return resultado

def subtracao(numero1=None, numero2=None):
    resultado = numero1 - numero2
    print(numero1," - ", numero2," = ", resultado)
    return resultado

def multiplicacao(numero1=None, numero2=None):
    resultado = numero1 * numero2
    print(numero1," * ", numero2," = ", resultado)
    return resultado

def divisao(numero1=None, numero2=None):
    resultado = numero1 / numero2
    print(numero1," / ", numero2," = ", resultado)
    return resultado

