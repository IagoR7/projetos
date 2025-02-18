recebimento1p =[]
recebimento2p = []
recebimento1r = []
recebimento2r =[]
meses = int(input("Digite a quantidade de meses: "))
for i in range(meses):
    valor = float(input(f"Digite a {i+1}º previsão: "))
    recebimento1p.append(valor)
for i in range(meses):
    valor = float(input(f"Digite a {i+1}º previsão: "))
    recebimento2p.append(valor)
for i in range(meses):
    valor = float(input(f"Digite o {i+1}º pagamento de entrada realizado: "))
    recebimento1r.append(valor)
for i in range(meses):
    valor = float(input(f"Digite o {i+1}º pagamento de entrada realizado: "))
    recebimento2r.append(valor)

tentp = recebimento1p[0] + recebimento2p[0]
tentr = recebimento1r[0] + recebimento2r[0]
print (f'total de entradas de previsão é {tentp} e de realizados é {tentr}')
forne = float(input("Digite o pamento total com o fornedor: "))
fpag = float(input("Digite o pamento total com a folha do pagamento: "))
aluguel = float(input("Digite o pamento total com o aluguel: "))
luz = float(input("Digite o pamento total com a luz: "))
fgts = float(input("Digite o pamento total com o fgts: "))

tudo = forne + fpag + aluguel + luz + fgts

totalp = tentp - tudo
totalr = tentr - tudo

print(f'O saldo final da previsão é {totalp} e o saldo final realizado é {totalr}')

