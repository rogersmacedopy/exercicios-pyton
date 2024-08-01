from datetime import date
atual = date.today().year
totimaior = 0
totmenor = 0
for pess in range (1, 8):
    nasc = int(input(f'Em que ano a pessoa {pess}ª nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totimaior += 1
    else:
       totmenor += 1
print(f'Ao todo tivemos {totimaior} pessoas maior de idade')
print(f'E também tivemos {totmenor} pessoas menor de idade')


