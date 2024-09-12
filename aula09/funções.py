#IMC
def calculo(peso,altura,imc):
    total = imc



peso = float(input("Digite o seu Peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso/(altura*altura)
    
if (imc <18.5):
        print("Magro")
elif (imc>18.5 and 24.9):
        print("Normal")
elif (imc>25.0 and  30.0):
        print("sobrepeso")
else:
        print("obesidade")
        
        
calculo(peso,altura,imc)
