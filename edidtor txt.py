# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao td (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print(nome.find(' '))



