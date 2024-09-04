#Crie um programa que lê uma lista de 10 números e conta a quantidade de números
#positivos e a quantidade de números negativos, e mostra o vetor com os negativos e o
#a soma dos positivos

negativos = []
soma_positivos = 0

print("Insira 10 números:")
for _ in range(10):
    numero = float(input())  # Recebe um número e o converte para float
    if numero < 0:
        negativos.append(numero)  # Adiciona número à lista de negativos
    elif numero > 0:
        soma_positivos += numero  # Soma os números positivos

# Conta a quantidade de números negativos
qtd_negativos = len(negativos)

# Exibe os resultados
print(f"Números negativos: {negativos}")
print(f"Quantidade de negativos: {qtd_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")