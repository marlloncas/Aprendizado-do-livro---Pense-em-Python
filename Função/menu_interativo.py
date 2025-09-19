def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Dizer Olá")
        print("2 - Calcular soma")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite seu nome: ")
            print("Olá,", nome, "!")
        elif escolha == "2":
            x = int(input("Digite o primeiro número: "))
            y = int(input("Digite o segundo número: "))
            print("Soma =", x + y)
        elif escolha == "3":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida!")

menu()
