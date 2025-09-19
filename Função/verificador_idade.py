def verificar_idade():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Bem-vindo,", nome, "! Você tem acesso liberado.")
    else:
        print("Desculpe,", nome, ". Acesso negado. Você é menor de idade.")

verificar_idade()
