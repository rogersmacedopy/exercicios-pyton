#023 - Separando dígitos de um número

'''num = int(input('informe um número : '))
n = str(num)
print('analisazndo o número {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Centena {}'.format(n[2]))
print('Dezena {}'.format(n[1]))
print('Milhar {}'.format(n[0]))'''

num = int(input('informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o número {}'.format(num))
print('unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('centena: {}'.format(c))
print('Milhar: {}'.format(m))
