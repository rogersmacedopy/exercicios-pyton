# 082 - Dividindo valores em várias listas

valores = list()
while True:
    valores.append(int(input('Digite um número: ').strip()))
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar [S/N]? ').strip().upper()[0]
    if resposta == 'N':
        break
pares = list(valor for valor in valores if valor % 2 == 0)
impares = list(valor for valor in valores if valor % 2 == 1)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')