#leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite um nome completo: ')).strip()

#eu
print(f'Seu nome tem Silva? {("silva" in nome.lower())}')

#sugestão curso em vídeo
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

#terceira via kk

print(f'Seu nome tem Silva? {nome.find()}')




