def tabuada():
    while True:
        n = int(input("Digite um número para ver a tabuada: "))
        for i in range(1, 11):
            print(n, "x", i, "=", n * i)

        repetir = input("Deseja ver a tabuada de outro número? (s/n): ")
        if repetir.lower() != "s":
            print("Encerrando programa...")
            break

tabuada()
