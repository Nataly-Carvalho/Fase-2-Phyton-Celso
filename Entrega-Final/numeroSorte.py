import random
import time

def numero_da_sorte():
    cont = 0
    chances = 5

    palpite = 0
    numero_da_sorte = random.randint(1, 10)
    print("=========================================================")
    print("=============🎮 Vamos iniciar o jogo 🎮===================")
    print("=🤖 Você deve acertar o número que o robô está pensando 🤖=")
    print("==========================================================")

    for i in range(5, 0, -1):
        print(f"O jogo vai começar em {i} segundos...✨")
        time.sleep(1)

    while palpite != numero_da_sorte and cont < chances:
        chances_restantes = chances - cont
        palpite = int(input(f"Digite um número, você tem {chances_restantes} chances restantes 😖: "))

        if palpite == numero_da_sorte:
            print("🎉🎉🎉 Parabéns! Você acertou 🎉🎉🎉")
            break
        else:
            print("Tente novamente ❌")
            cont += 1
            if numero_da_sorte < palpite:
                print("Digite um número menor ⬇️")
            else:
                print("Digite um número maior ⬆️")

    if palpite != numero_da_sorte:
        print("☠️☠️☠️ GAME OVER ☠️☠️☠️")
        print(f"Suas chances acabaram! O número era {numero_da_sorte}")

if __name__ == "__main__":
    numero_da_sorte()
