frase = input("Digite uma frase: \n")

print("Maiúsculo:", frase.upper(), "\n")
print("Minúsculo:", frase.lower(), "\n")
print("Sem espaços extras:", frase.strip(), "\n")
print("Substituir Python por Programação:", frase.replace("Python", "Programação"), "\n")
print("Python está na frase?", "Python" in frase, "\n")

lista_palavras = frase.split()
print("Lista de palavras:", lista_palavras, "\n")
print("Frase unida:", " ".join(lista_palavras), "\n")
