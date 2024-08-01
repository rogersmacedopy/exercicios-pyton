#044 - Gerenciador de Pagamentos

print('{:=^40}'.format(' Lojas Rojão '))
preço = float(input('digite o valor da compra: '))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro  cheque
[2] à vista cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opição ?  '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('Sua compra sera parcelada em {}x de R${:.2f} SEM JUROS '.format(2, parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparç = int(input('Quantas parcelas'))
    parcela = total / totparç
    print('Sua compra será parcelada em {}x de R${:.2f} no final COM JUROS.'.format(totparç, parcela))
else:
    total = 0
    print('Opção invalida de pagamento. tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))




