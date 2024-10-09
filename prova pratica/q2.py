km = int(input('Digite a velocidade: '))
multa = 5

if km >80:
    taxa =(km-80)*multa
    print(f'Você foi multado em R$ {taxa:.2f}')