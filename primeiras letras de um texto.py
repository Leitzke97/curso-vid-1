# leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome de uma cidade: '))
print(cidade[:5].upper() == 'SANTO')
