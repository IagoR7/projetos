#Escreva um programa que leia números inteiros do usuário até que o número 0 seja digitado. Ao final, exiba a soma desses números.

numeros= []

print("Digite o valor 0 para terminar o progama")
while True:
    
    valor = int(input(f"Digite um valor: "))
    if (valor == 0):
        break
    else:
        numeros.append(valor)
        soma = sum(numeros)
print(f'A Soma dos progamas é {soma}')
 