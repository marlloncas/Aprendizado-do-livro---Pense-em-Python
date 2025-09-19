def sistema_funcionarios():
    funcionarios = [] 
    while True:
        print("\n=== MENU FUNCIONÁRIOS ===")
        print("1 - Adicionar funcionário")
        print("2 - Listar todos")
        print("3 - Buscar por setor")
        print("4 - Salário acima de um valor")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                setor = input("Setor: ")
                salario = float(input("Salário: "))
                funcionarios.append((nome, idade, setor, salario))
                print(f"{nome} adicionado(a) com sucesso!")

            case "2":
                if not funcionarios:
                    print("Nenhum funcionário cadastrado.")
                else:
                    print("\n=== Funcionários cadastrados ===")
                    for f in funcionarios:
                        print(f"Nome: {f[0]}, Idade: {f[1]}, Setor: {f[2]}, Salário: {f[3]}")

            case "3":
                setor_busca = input("Digite o setor para buscar: ")
                encontrados = [f for f in funcionarios if f[2].lower() == setor_busca.lower()]
                if not encontrados:
                    print(f"Nenhum funcionário encontrado no setor {setor_busca}.")
                else:
                    print(f"\nFuncionários no setor {setor_busca}:")
                    for f in encontrados:
                        print(f"Nome: {f[0]}, Idade: {f[1]}, Salário: {f[3]}")

            case "4":
                valor = float(input("Digite o valor do salário: "))
                encontrados = [f for f in funcionarios if f[3] > valor]
                if not encontrados:
                    print(f"Nenhum funcionário com salário acima de {valor}.")
                else:
                    print(f"\nFuncionários com salário acima de {valor}:")
                    for f in encontrados:
                        print(f"Nome: {f[0]}, Idade: {f[1]}, Setor: {f[2]}, Salário: {f[3]}")

            case "5":
                print("Saindo do sistema...")
                break

            case _:
                print("Opção inválida! Tente novamente.")

sistema_funcionarios()
