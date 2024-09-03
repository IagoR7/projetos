#Crie um programa que leia 10 números do usuário e armazene-os em uma lista. Em
#seguida, exiba a lista, o maior número contido nela, e a soma de todos os números
#digitados.

numeros = []

for i in range(10):
    valor = int(input(f"digite o valor {i+1}: "))
    
    
    numeros.append(valor)
maior = max (numeros)
soma = sum(numeros)
print(f'os numeros da lista são {numeros}')
print(f'O maior numero entre eles é o numeros {maior}')
print(f"E a soma desses numeros é {soma}")

