#Iago Ribeiro Neves Santos
#Breno Prado
#Turma: 3112

m1 = 200
m2 = 300
m3 = 400
m4 = 500

prodA = m1,m2,m3,m4

m1b = 500
m2b = 600
m3b = 700
m4b = 550

prodB = m1b,m2b,m3b,m4b

m1c = 600
m2c = 900
m3c = 1.200
m4c = 1.500

prodC = m1c,m2c,m3c,m4c

m1d = 700
m2d = 800
m3d = 1000
m4d = 1.500

prodD = m1d,m2d,m3d,m4d,



vmdA = ((m1+m2+m3+m4)/4)/25
vmdB = ((m1b+m2b+m3b+m4b)/4)/25
vmdC = ((m1c+m2c+m3c+m4c)/4)/25
vmdD = ((m1d+m2d+m3d+m4d)/4)/25 

trA = 5
trB = 6
trC = 7
trD = 8

eminA = trA*vmdA
eminB = trB*vmdB
eminC = trC*vmdC
eminD = trD*vmdD

lrA = 60
lrB = 70
lrC = 80
lrD = 90

emaxA = lrA+ eminA
emaxB = lrB+ eminB
emaxC = lrC+ eminC
emaxD = lrD+ eminD


eaA = 100
if eaA < eminA:
    print('Comprar')
else: print('Não Comprar')


eaB = 90
if eaB < eminB:
    print('Comprar')
else: print('Não Comprar')

eaC = 120
if eaC < eminC:
    print('Comprar')
else: print('Não Comprar')

eaD = 80
if eaD < eminA:
    print('Comprar')
else: print('Não Comprar')

