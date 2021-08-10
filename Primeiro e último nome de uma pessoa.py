#Primeiro e último nome de uma pessoa

nomeCompleto = (input('Digite seu nome completo: ')).strip()
nome = nomeCompleto.split()
print(f'Seu primeiro nome é: {(nome[0])}')
print(f'Seu último nome é: {nome[len(nome)-1]}')

#curso em vídeo
print('seu primeiro nome é {}'.format(nome[0]))
print('seu último nome é {}'.format(nome[len(nome)-1]))