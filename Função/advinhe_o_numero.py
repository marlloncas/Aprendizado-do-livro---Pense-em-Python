import random

def jogo_adivinhacao():
    while True:
        numero_secreto = random.randint(1, 10)
        tentativas = 0

        while True:
            palpite = int(input("Adivinhe o número (1 a 10): "))
            tentativas += 1

            if palpite == numero_secreto:
                print("Parabéns! Você acertou em", tentativas, "tentativas.")
                break
            elif palpite < numero_secreto:
                print("Tente um número maior!")
            else:
                print("Tente um número menor!")

        repetir = input("Deseja tentar mais uma vez? (s/n): ")
        if repetir.lower() != "s":
            print("Certo!... Finalizando o programa")
            break 

jogo_adivinhacao()
