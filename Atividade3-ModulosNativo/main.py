import datetime
import modulosNativos

while True:
    modulosNativos.menu()
    op = input("Selecione a operação: ")

    if op == "1" or op == "2" or op == "3" or op == "5":
        if op == "1":
            numero = 8
            print(f"A raiz quadrada de {numero} é {modulosNativos.calcular_raiz_quadrada(numero)}")
            print(f"O fatorial de {numero} é {modulosNativos.calcular_fatorial(numero)}")
        elif op == "2":
            data_atual = modulosNativos.mostrar_data_hora_atual()
            print(f"Data e hora atuais: {data_atual}")

            data1 = datetime.date(2024, 8, 1)
            data2 = datetime.date(2024, 8, 10)
            print(
                f"A diferença entre {data1} e {data2} é de {modulosNativos.calcular_diferenca_datas(data1, data2)} dias.")

        elif op == "3":
            numero_aleatorio = modulosNativos.gerar_numero_aleatorio(1, 100)
            print(f"Número aleatório entre 1 e 100: {numero_aleatorio}")

            itens = ['maçã', 'banana', 'laranja', 'uva']
            item_escolhido = modulosNativos.escolher_item_aleatorio(itens)
            print(f"Item escolhido aleatoriamente: {item_escolhido}")

    elif op == "4":
        print("Saindo...")
        break

    else:
        print('Valor inválido, por favor selecione uma opção válida.')

    input("Pressione Enter para continuar...")

