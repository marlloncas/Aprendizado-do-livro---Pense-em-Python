def agenda():
    contatos = {}

    while True:
        print("\n=== MENU AGENDA ===")
        print("1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Buscar contato")
        print("4 - Listar todos")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            contatos[nome] = telefone
            print(f"{nome} foi adicionado com o telefone {telefone}.")

        elif opcao == "2":
            nome = input("Digite o nome para remover: ")
            if nome in contatos:
                del contatos[nome]
                print(f"{nome} foi removido da agenda.")
            else:
                print("Contato não encontrado.")

        elif opcao == "3":
            nome = input("Digite o nome para buscar: ")
            if nome in contatos:
                print(f"Telefone de {nome}: {contatos[nome]}")
            else:
                print("Contato não encontrado.")

        elif opcao == "4":
            if len(contatos) == 0:
                print("Agenda vazia.")
            else:
                print("=== Contatos ===")
                for nome, telefone in contatos.items():
                    print(f"{nome} -> {telefone}")

        elif opcao == "5":
            print("Saindo... até logo!")
            break

        else:
            print("Opção inválida, tente de novo!")
agenda()
