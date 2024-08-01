#017 - Catetos e Hipotenusa

'''co = float(input('Qual é a medida do cateto oposto '))
ca = float(input('Qual é a medida do cateto adjacente '))
hip = (co **2 + ca**2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))'''

import math
co = float(input('Qual é a medida do cateto oposto: '))
ca = float(input('Qual a medida do cateto adjasente: '))
hip = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}.'.format(hip))


