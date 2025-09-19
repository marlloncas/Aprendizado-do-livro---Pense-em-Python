def cadastro_alunos():
    alunos = [] #lista vazia

    for i in range(3):
        nome = input(f"Digite o nome do aluno {i+1}: ")
        idade = int(input(f"Digite a idade do aluno {i+1}: "))
        alunos.append((nome, idade))  #adiciona uma tupla à lista

    print("\nAlunos cadastrados:")
    for indice, (nome, idade) in enumerate(alunos): #Mostrar os alunos cadastrados
        print(f"{indice} - {nome} ({idade} anos)")

    
    indice = int(input("\nDigite o índice do aluno que deseja consultar: "))
    if 0 <= indice < len(alunos):
        nome, idade = alunos[indice]
        print(f"Aluno selecionado: {nome} ({idade} anos)")
    else:
        print("Índice inválido!")

    
    print("\nAlunos com 20 anos ou mais:")
    for nome, idade in alunos:
        if idade >= 20:
            print(f"{nome} ({idade} anos)")


cadastro_alunos()
