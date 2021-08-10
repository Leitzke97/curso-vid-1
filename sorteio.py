import random
n1 = str(input('Digite o nome 1: '))
n2 = str(input('Digite o nome 2: '))
n3 = str(input('Digite o nome 3: '))
n4 = str(input('Digite o nome 4: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)