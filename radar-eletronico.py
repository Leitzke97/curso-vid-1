# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre
# #uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual a sua velocidade?'))
multa = (vel - 80) * 7
if vel > 80:
    print(f'você foi multado em {multa:.2f}')
else:
    print('siga')