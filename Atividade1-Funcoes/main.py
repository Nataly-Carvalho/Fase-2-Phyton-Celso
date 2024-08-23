import funcoes

while True:
    funcoes.menu()
    op = input("Selecione a operação: ")

    if op == "1" or op == "2" or op == "3" or op == "4":
        numero1 = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o segundo número: '))

        if op == "1":
            funcoes.soma(numero1=numero1, numero2=numero2)
        elif op == "2":
            funcoes.subtracao(numero1=numero1, numero2=numero2)
        elif op == "3":
            funcoes.divisao(numero1=numero1, numero2=numero2)
        elif op == "4":
            funcoes.multiplicacao(numero1=numero1, numero2=numero2)
    elif op == "5":
        print("Saindo...")
        break
    else:
        print('Valor inválido, por favor selecione uma opção válida.')

    input("Pressione Enter para continuar...")

