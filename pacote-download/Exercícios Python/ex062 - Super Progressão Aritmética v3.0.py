#Super Progressão Aritmética v3.0

p = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
i = 0
op = terms = 1
while op != 0:
    while i < (10 + terms):
        pa = p + (i - 1) * r
        print(pa, end= ' -> ')
        i += 1
    res = print('FIM', end= '')
    op = terms
    terms += int(input('\nQuantos termos a mais você quer mostrar? '))
    op = terms - op