#015 - Aluguel de Carros

dia = int(input('Quantos dias de carro alugado'))
km = float(input('Quantos KM o carro andou'))
resul = dia * 60
resul2 = km * 0.15
total = resul + resul2
print(f'você ficou {dia} dias com o carro e andou {km}km o total a pagar é {total}')