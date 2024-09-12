#usando vetor e funções crie um algoritmo que recebe 6 numeros e armazena em um vetor e a função esse vetor e mostrar somente os numero que são impares

def impar(impares):
    for x in impares:
        if x %2==1:
            print(x)


impares = []
for i in range (6):
    numeros = int(input("Digite Um numero: "))
    impares.append(numeros)



impar(impares)
