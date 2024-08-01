#041 - Classificando Atletas

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('categoria Mirim')
elif idade <= 14:
    print('categoria Infantil')
elif idade <= 19:
    print('categoria Juvenil')
elif idade <= 25:
    print('categoria Sênior')
else:
    print('Categoria Master')
