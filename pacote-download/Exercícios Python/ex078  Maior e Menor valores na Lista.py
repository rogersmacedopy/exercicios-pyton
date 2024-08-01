#078 - Maior e Menor valores na Lista

'''listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para posição {c}: ')))
    if c ==0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('=-' * 30)
print(f'Voce digitiu os valores {listanum}')
print(f'o mair valor digitado foi{mai}', end='')
for i, v in enumerate(listanum):
    if v ==mai:
        print(f'{i}...', end='')
print(f'O menor valor digitado foi {men}', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()'''

val = [int(input('Primeiro valor: ')), int(input('Segundo valor: ')),
       int(input('Terceiro valor: ')), int(input('Quarto valor: ')),
       int(input('Quinto valor: '))]
print(f'O maior valor é {max(val)} que está na posição {val.index(max(val))+1}.')
print(f'O menor valor é {min(val)} que está na posição {val.index(min(val))+1}.')
