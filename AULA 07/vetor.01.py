#heroi = []
#while True:
#contador = contador +1
   #personagem = input(f'digite o personagem {contador}: ')
   #if (personagem.lower() == 'sair'):
    #  break
   #else:
    #  heroi.append(personagem)
#print(heroi)



#personagens = []
#for i in range (5):
   # heroi = input("Diga o nome de um heroi: ")
   # personagens.append(heroi)

#print(personagens)

#armazene 10 numeros em um vetor e depois imprima somente os que são pares
numeros = []

for i in range(10):
   valor = int(input(f"Digite o numero {i+1}: "))
   numeros.append(valor)


for par in numeros:
    if par % 2 == 0:
        print(par)
   

