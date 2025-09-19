def bloco_de_notas():
    nome_arquivo = "notas.txt"

    while True:
        print("\n=== BLOCO DE NOTAS ===")
        print("1 - Escrever no arquivo")
        print("2 - Ler arquivo")
        print("3 - Apagar arquivo")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            texto = input("Digite o texto: ")
            with open(nome_arquivo, "a") as arquivo:  # "a" = acrescentar
                arquivo.write(texto + "\n")
            print("Texto salvo com sucesso!")

        elif opcao == "2":
            try:
                with open(nome_arquivo, "r") as arquivo:
                    conteudo = arquivo.read()
                    if conteudo.strip() == "":
                        print("O arquivo está vazio.")
                    else:
                        print("\n=== Conteúdo do arquivo ===")
                        print(conteudo)
            except FileNotFoundError:
                print("Arquivo não encontrado.")

        elif opcao == "3":
            with open(nome_arquivo, "w") as arquivo:  # sobrescreve com vazio
                arquivo.write("")
            print("Arquivo apagado com sucesso!")

        elif opcao == "4":
            print("Saindo... até logo!")
            break

        else:
            print("Opção inválida, tente de novo!")

bloco_de_notas()
