def soma_numeros():
    while True:
        soma = 0
        while True:
            numero = int(input("Digite um número (0 para sair): "))
            if numero == 0:
                break
            soma += numero
        print("A soma total é:", soma)

        repetir = input("Deseja somar outro grupo de números? (s/n): ")
        if repetir.lower() != "s":
            print("Encerrando programa...")
            break

soma_numeros()
