#039 - Alistamento Militar

from datetime import date
atual = date.today() . year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {}anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade > 18:
    saldo = 18 - idade
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento foi em {} ano'.format(ano))
elif idade < 18:
    saldo = idade + 18
    print('Você ainada não tem 18 anos. Ainda faltam {} para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} ano!'.format(ano))

