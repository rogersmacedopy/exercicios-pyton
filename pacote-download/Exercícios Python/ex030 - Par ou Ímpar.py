#030 - Par ou Ímpar?

num = int(input('Me diga um número qualquer: '))
resul = num % 2
if resul == 0:
 print('O resultado {} é par'.format(num))
else:
 print('O resultado {} é impar'.format(num))
