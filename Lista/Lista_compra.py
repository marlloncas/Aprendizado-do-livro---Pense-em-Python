def lista_de_compras():
    compras = []

    while True:
        print("\n=== MENU LISTA DE COMPRAS ===")
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Mostrar lista")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            item = input("Digite o item para adicionar: ")
            compras.append(item)
            print(item, "foi adicionado à lista!")

        elif opcao == "2":
            item = input("Digite o item para remover: ")
            if item in compras:
                compras.remove(item)
                print(item, "foi removido da lista!")
            else:
                print("Esse item não está na lista!")

        elif opcao == "3":
            if len(compras) == 0:
                print("A lista está vazia.")
            else:
                print("Sua lista de compras:")
                for i, item in enumerate(compras, 1):
                    print(i, "-", item)

        elif opcao == "4":
            print("Saindo... até logo!")
            break

        else:
            print("Opção inválida, tente de novo!")

lista_de_compras()
