#crie um progama que receba três números e imprima o maior deles
numeros= []

for i in range(3):
    valor = int(input(f"Digite o valor {i+1}: "))

numeros.append(valor)

maior = max (numeros)
print(maior)