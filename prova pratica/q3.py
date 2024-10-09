def viagem():
    km= int(input('Digite a distancia: '))
    if km <=200:
        preco = 0.50
        km2 = km*preco
        print (f'O valor da passagem é de R$ {km2:.2f}')
    else:
        preco2 = 0.45
        km3 = km*preco2
        print(f'O valor da passagem é de R$ {km3:.2f}')

viagem()