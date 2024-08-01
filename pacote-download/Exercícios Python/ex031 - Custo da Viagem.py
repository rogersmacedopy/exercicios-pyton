#031 - Custo da Viagem

#Passagem = R$0,50 por Km para viagens até 200Km
#R$ 0,45 para viagens mais longas
'''km = float(input('Qual a distância da sua vagem ? '))
print('Você está preste a percorrer uma viagem de {}Km'.format(km))
if km >= 200:
    print('O preço da sua Viagem será R${:.2f}'.format(km * 0.45))
else:
    km <= 200
    print('O preço da sua Viagem será R${:.2f}'.format(km * 0.50))'''

km = float(input('Qual a distância da sua vagem ? '))
print('Você está preste a percorrer uma viagem de {}Km'.format(km))
preço = km * 0.50 if km <= 200 else km * 0.45
print('O preço da sua Viagem será R${:.2f}'.format(preço))