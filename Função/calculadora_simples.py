def calculadora():
    while True:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        op = input("Digite a operação (+, -, *, /): ")

        if op == "+":
            print("Resultado:", x + y)
        elif op == "-":
            print("Resultado:", x - y)
        elif op == "*":
            print("Resultado:", x * y)
        elif op == "/":
            if y != 0:
                print("Resultado:", x / y)
            else:
                print("Erro: divisão por zero!")
        else:
            print("Operação inválida")

        repetir = input("Deseja calcular outro número? (s/n): ")
        if repetir.lower() != "s":
            print("Encerrando o programa...")
            break

calculadora()
