valor = float(input("Digite o valor da casa:"))
salario = float(input("Digite o seu salario: "))
anos = int(input("Digite a quantidades de anos a pagar: "))

meses = anos*12
valordivido = (valor/meses)

if valordivido >= 0.3*salario:
    print("infelizmente voce nao pode pegar o emprestimo")
else:
    print("emprestimo ok")