from math import hypot
op = float(input('Digite o cateto oposto: '))
ad = float(input('Digite o cateto adjacente: '))

hi = hypot(op, ad)

print(f'O valor da hipotenusa é de {hi}')
