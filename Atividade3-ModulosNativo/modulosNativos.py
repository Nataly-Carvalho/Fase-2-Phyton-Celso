import math
import random
import datetime

def menu():
    print("----------------------------------")
    print("========== Calculadora ===========")
    print("------------ 1 - Math ------------")
    print("---------- 2 - Date Time ---------")
    print("----------- 3 - Random -----------")
    print("----------- 4 - Sair -------------")
    print("----------------------------------")

def calcular_raiz_quadrada(numero):
    return math.sqrt(numero)

def calcular_fatorial(numero):
    return math.factorial(numero)

def mostrar_data_hora_atual():
    agora = datetime.datetime.now()
    return agora.strftime("%Y-%m-%d %H:%M:%S")

def calcular_diferenca_datas(data1, data2):
    delta = data2 - data1
    return delta.days

def gerar_numero_aleatorio(inicio, fim):
    return random.randint(inicio, fim)

def escolher_item_aleatorio(lista):
    return random.choice(lista)


