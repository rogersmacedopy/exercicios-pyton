#048 - Soma ímpares múltiplos de três

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1  #contador  ou cont += 1
        soma = soma + c  #acumulador ou soma += 1
print('A soma de todos os valores {} é {}'.format(cont ,soma))
