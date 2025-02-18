# import math
# lec = (2*3000*130)/ (0.25*25)
# raiz_quadrada = math.sqrt(lec)

# #valores para formula
# ca = 3000
# cc = 130
# cpa = 0.25
# pu = 25


# a1 = 100
# a2 = raiz_quadrada
# a3 = 1000

# b1 = ca/a1
# b2 = ca/a2
# b3 = ca/a3

# c1= a1/2*pu
# c2 = a2/2*pu
# c3 = a3/2*pu

# d1 = cpa*c1
# d2 = cpa*c2
# d3 = cpa*c3

# e1 = cc*b1
# e2 = cc*b2
# e3 = cc*b3

# f1 = d1+e1
# f2 = d2+e2
# f3 = d3+e3

# print(f'Os resultados para a coluna A: {a1,a2,a3}')
# print(f'Os resultados para a coluna B: {b1,b2,b3}')
# print(f'Os resultados para a coluna C: {c1,c2,c3}')
# print(f'Os resultados para a coluna D: {d1,d2,d3}')
# print(f'Os resultados para a coluna E: {e1,e2,e3}')
# print(f'Os resultados para a coluna F: {f1,f2,f3}')


import math

# Cálculo inicial
lec = (2 * 3000 * 130) / (0.25 * 25)
raiz_quadrada = math.sqrt(lec)

# Valores para a fórmula
ca = 3000
cc = 130
cpa = 0.25
pu = 25

# Coluna A
a1 = 100
a2 = raiz_quadrada
a3 = 1000

# Coluna B
b1 = ca / a1
b2 = ca / a2
b3 = ca / a3

# Coluna C
c1 = a1 / 2 * pu
c2 = a2 / 2 * pu
c3 = a3 / 2 * pu

# Coluna D
d1 = cpa * c1
d2 = cpa * c2
d3 = cpa * c3

# Coluna E
e1 = cc * b1
e2 = cc * b2
e3 = cc * b3

# Coluna F
f1 = d1 + e1
f2 = d2 + e2
f3 = d3 + e3

# Exibindo resultados como tabela
print(f"{'Coluna A':<10} {'Coluna B':<15} {'Coluna C':<15} {'Coluna D':<15} {'Coluna E':<15} {'Coluna F':<15}")
print("-" * 83)
print(f"{a1:<10} {b1:<15.2f} {c1:<15.2f} {d1:<15.2f} {e1:<15.2f} {f1:<15.2f}")
print(f"{a2:<10.2f} {b2:<15.2f} {c2:<15.2f} {d2:<15.2f} {e2:<15.2f} {f2:<15.2f}")
print(f"{a3:<10} {b3:<15.2f} {c3:<15.2f} {d3:<15.2f} {e3:<15.2f} {f3:<15.2f}")
