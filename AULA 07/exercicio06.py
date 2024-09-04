#Crie um programa em Python que lê uma lista de 10 nomes e sorteia um nome entre
#eles.

import random

nomes = ['iago','joao','paulo','erika','gabriel','pedrinho','clodoado','juracy','bruna','luisa']

sortudo = random.choice(nomes)
print(sortudo)