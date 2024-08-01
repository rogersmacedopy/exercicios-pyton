#Estatísticas em produtos

cp = total = maior = menor = 0
print('-==-' * 6)
print('   Lojas armazenagem')
print('-==-' * 6)
while True:
    cp += 1
    produto = str(input(f'Digite o nome do {cp} produto: ')).lower()
    preço = float(input(f'Digite o preço da(o) {produto}: R$'))
    q = str(input('Quer continuar? [S/N]: ')).upper()
    if cp == 1:
        menor = preço
        pb = produto
    else:
        if preço < menor:
            menor = preço
            pb = produto
    if q != 'S' and q != 'N':
        while q != 'S' and q != 'N':
            q = str(input('Tente novamente: Quer continuar? [S/N]: ')).upper()
    total += preço
    if preço >= 1000:
        maior += 1
    if q == 'N':
        break
if cp > 1:
    print(f'O total a ser pago é de R${total:.2f}.')
    print(f'Existem {maior} produtos que custam mais de 1000 reais.')
    if menor < 2:
        print(f'O produto mais barato foi o(a) {pb}, que custa {menor:.2f} real.')
    elif menor > 1:
        print(f'O produto mais barato foi o(a) {pb}, que custa {menor:.2f} reais.')
elif cp < 2:
    print(f'O total a ser pago é de R${total:.2f}.')
    print(f'Existe {maior} produto que custa mais de 1000 reais.')
    if menor < 2:
        print(f'O produto mais barato foi o(a) {pb}, que custa {menor:.2f} real.')
    elif menor > 1:
        print(f'O produto mais barato foi o(a) {pb}, que custa {menor:.2f} reais.')
print('<---Programa encerrado--->')