forne = 20.000
fpag = 40.000
aluguel = 5.000
luz = 1.000
fgts = 5.000

tudo = forne + fpag + aluguel + luz + fgts


recebimento1p =[]
recebimento2p = []
recebimento1r = []
recebimento2r =[]
for i in range(1):
    valor = int(input(f"Digite a primeira revisão: "))
    recebimento1p.append(valor)
for i in range(1):
    valor = int(input(f"Digite a segunda revisão: "))
    recebimento2p.append(valor)
for i in range(1):
    valor = int(input(f"Digite o primeiro recebimento: "))
    recebimento1r.append(valor)
for i in range(1):
    valor = int(input(f"Digite o segundo recebimento: "))
    recebimento2r.append(valor)

tent = recebimento1p[0] + recebimento2p[0], recebimento1r[0] + recebimento2r[0]
print (f'total de entradas de previsão e realizado é:  {tent}')
forne = float(input("Digite o pamento total com o fornedor"))
fpag = float(input("Digite o pamento total com o fornedor"))
aluguel = float(input("Digite o pamento total com o fornedor"))
luz = float(input("Digite o pamento total com o fornedor"))
fgts = float(input("Digite o pamento total com o fornedor"))

