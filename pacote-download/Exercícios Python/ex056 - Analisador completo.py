#056 - Analisador completo

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'----{p}ª pessoa-----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('SEXO: [M/F]:')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade < maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade:.2f} anos. ')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomemaisvelho}.')
print(f'Ao total são {totmulher20} mulhere com menos de 20 anos. ')
