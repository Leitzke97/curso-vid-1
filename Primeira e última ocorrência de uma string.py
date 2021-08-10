#um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ').strip().lower())
print(f'Mostre quantas vezes a parece a letra a: {frase.count("a")}')
print(f'A primeira letra a aparece na posição: {frase.find("a")+1}')
print(f'A última letra a aparece na posição:{frase.rfind("a")+1}')
