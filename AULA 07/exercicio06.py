#Crie um programa em Python que lê uma lista de 10 nomes e sorteia um nome entre
#eles.

import random

nomes = []

for i in range(10):
    sorte = input('DIGITE UM NOME: ')
    nomes.append(sorte)

sortudo = random.choice(nomes)
print(sortudo)
