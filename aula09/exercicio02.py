import random
def camp(lista):
    vencedor = random.choice(lista)
    print(vencedor)

lista = []
for i in range (10):
    times = input("Digite um time: ")
    lista.append(times)
    
camp(lista)