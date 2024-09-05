#Crie um programa em Python que lê uma lista de 10 nomes e sorteia um nome entre
#eles.

import random

alunos = []

while True:
    sorte = input('DIGITE UM NOME: ')
    if (sorte.lower == "sair"):
        break
    else:
        alunos.append(sorte)

sortudo = random.choice(alunos)
print(sortudo)