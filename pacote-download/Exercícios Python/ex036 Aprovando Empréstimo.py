#036 - Aprovando Empréstimo

casa = float(input('Valor da Casa: R$'))
salário = float(input('salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento ?'))
mínimo = salário * 30/100
prestação = casa / (anos * 12)
print('para pagar uma casa de {:.2f} em {} anos '.format(casa, anos), end ='')
print('A prestação será de R$ {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo negado!')



