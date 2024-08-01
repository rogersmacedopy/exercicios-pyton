frase = str(input('digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
print('Você digitou a frase {}'.format(junto))
'''inverso = '''''
inverso = junto[::-1]
'''for letra in range(len(junto)- 1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')
