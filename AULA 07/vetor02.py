#peça ao usuario para digitar 8 numeros e apos digitar os numeros imprima a soma de todos os numeros digitados
numeros = []

for i in range(8):
   valor = int(input(f"Digite o numero {i+1}: "))
   
   
   numeros.append(valor)

soma = sum(numeros)
print(soma)