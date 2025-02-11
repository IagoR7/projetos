m1 = 100
m2 = 100
m3 = 100

prodA = m1,m2,m3

m1b = 200
m2b = 200
m3b = 200

prodB = m1b,m2b,m3b

m1c = 400
m2c = 400
m3c = 400

prodC = m1c,m2c,m3c

vmdA = ((m1+m2+m3)/3)/25
vmdB = ((m1b+m2b+m3b)/3)/25
vmdC = ((m1c+m2c+m3c)/3)/25


tr = int(input("Digite o Tempo de Reposição: "))

eminA = tr*vmdA
eminB = tr*vmdB
eminC = tr*vmdC

lr = int(input("Digite o Lote Reposição: "))

emaxA = lr+ eminA
emaxB = lr+ eminB
emaxC = lr+ eminC


eaA = int(input("Digite o Estoque Atual A: "))

if eaA < eminA:
    print('Comprar')
else: print('Não Comprar')


eaB = int(input("Digite o Estoque Atual B: "))

if eaB < eminB:
    print('Comprar')
else: print('Não Comprar')

eaC = int(input("Digite o Estoque Atual C: "))

if eaC < eminC:
    print('Comprar')
else: print('Não Comprar')

