from math import sin, cos, radians, tan
ang = float(input('Digite o angulo que você deseja: '))
sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print(f'Para o ângulo de {ang} SENO tem valor de {sen:.2f}')
print(f'Para o ângulo de {ang} COSSENO tem valor de {coss:.2f}')
print(f'Para o ângulo de {ang} TANGENTE tem valor de {tang:.2f}')
