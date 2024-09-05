numeros = []

for i in range(10):
    valor = int(input('Digite um numero:'))
    numeros.append(valor)

midia = len(numeros)
soma = sum(numeros)
media = soma/midia
print(f'A media dos valores é {media}')
