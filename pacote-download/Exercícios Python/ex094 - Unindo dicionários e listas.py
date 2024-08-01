#094 - Unindo dicionários e listas

dados = dict()
pessoas = list()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] '))
    while dados['sexo'] not in 'MmFf':
        dados['sexo'] = str(input('Por favor, digite apenas M ou F. '))
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    continuar = str(input('Quer continuar? [S/N] '))
    pessoas.append(dados.copy())
    while continuar not in 'SsNn':
        continuar = str(input('Por favor, digite apenas S ou N. '))
    if continuar in 'Nn':
        break
print('-' * 72)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas')
media = soma / len(pessoas)
print(f'A média de idade é de {media} anos')
print('As mulheres cadastradas foram', end=' ')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('Lista de pessoas que estão com a idade acima da média:', end=' ')
for p in pessoas:
    if p['idade'] > media:
        print(f'{p["nome"]}', end=' ')
    else:
        print('Todos estão dentro da media', end=' ')
print()
print('\n<= ENCERRANDO =>')