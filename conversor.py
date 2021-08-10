Controle = 1
while True:
    print('Converão em Criptomoeda')
    print('1-converter bitcoins para reais:')
    print('2-converter reais para bitcoins:')
    print('3-Sair')
    controle = int(input('Escolha uma opção:'))
    if controle == 3:
        break
    print('_______________________', end='\n')
    if controle == 1:
        num_01 = float(input('Digite um valor de bitcoins: '))
        num_02 = float(input('Digite o valor da cotação em reais: '))
        print('\n{0:.2f} bitcoins valem R${1:.2f}'.format(num_01, num_01*num_02))
        print('_______________________', end='\n')
    elif controle == 2:
        num_01 = float(input('Digite um valor de reais: '))
        num_02 = float(input('Digite o valor da cotação em reais: '))
        print('\n{0:.2f} valem R${1:.2f}'.format(num_01, num_01/num_02))
        print('_______________________', end='\n')
print('_______________________', end='\n')
print('Fim da conversão')
