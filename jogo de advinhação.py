from random import randint

comp = randint(0, 5)
print('----'*17)
print('Vamos ver se você consegue advinhar o número que eu estou pensando?')
print('----'*17)
num = int(input('Digite um número de 0 a 5:'))
if comp == num:
    print('----' * 17)
    print('cê é bichão mesmo hein')
    print('----' * 17)
else:
    print('----' * 17)
    print('e ainda dizem que a sua raça domina a razão...')
    print('----' * 17)

