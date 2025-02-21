#Iago Ribeiro Neves Santos
#Breno Prado
#Turma: 3112
import math

# Cálculo inicial
lec = (2 * 4000 * 150) / (0.30 * 35)
raiz_quadrada = math.sqrt(lec)

# Valores para a fórmula
ca = 4000
cc = 150
cpa = 0.30
pu = 35

# Coluna A
a1 = 100
a2 = raiz_quadrada
a3 = 1000
a4 = 2000

# Coluna B
b1 = ca / a1
b2 = ca / a2
b3 = ca / a3
b4 = ca / a4

# Coluna C
c1 = a1 / 2 * pu
c2 = a2 / 2 * pu
c3 = a3 / 2 * pu
c4 = a4 / 2 * pu

# Coluna D
d1 = cpa * c1
d2 = cpa * c2
d3 = cpa * c3
d4 = cpa * c4

# Coluna E
e1 = cc * b1
e2 = cc * b2
e3 = cc * b3
e4 = cc * b4

# Coluna F
f1 = d1 + e1
f2 = d2 + e2
f3 = d3 + e3
f4 = d4 = e4

# Exibindo resultados como tabela
print(f"{'Coluna A':<10} {'Coluna B':<15} {'Coluna C':<15} {'Coluna D':<15} {'Coluna E':<15} {'Coluna F':<15}")
print("-" * 83)
print(f"{a1:<10} {b1:<15.2f} {c1:<15.2f} {d1:<15.2f} {e1:<15.2f} {f1:<15.2f}")
print(f"{a2:<10.2f} {b2:<15.2f} {c2:<15.2f} {d2:<15.2f} {e2:<15.2f} {f2:<15.2f}")
print(f"{a3:<10} {b3:<15.2f} {c3:<15.2f} {d3:<15.2f} {e3:<15.2f} {f3:<15.2f}")
print(f"{a4:<10} {b4:<15.2f} {c4:<15.2f} {d4:<15.2f} {e4:<15.2f} {f4:<15.2f}")
