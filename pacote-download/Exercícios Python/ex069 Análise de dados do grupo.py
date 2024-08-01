#Análise de dados do grupo

cont18 = conth = contm20 = 0
while True:
    print('-'*30)
    print('\tCADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('SEXO ÍNVALIDO. Tende novamente.')
    else:
        if sexo == 'M' or 'F' and idade >= 18:
            cont18 += 1
        if sexo == 'M':
            conth += 1
        if sexo == 'F' and idade <= 20:
            contm20 += 1
    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont18}\nAo todo temos {conth} Homens cadastrados\nE temos {contm20} mulheres com menos de 20 anos')
