#016 - Quebrando um número

'''import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {}, e sua porção inteira é {}'.format(num, math.trunc(num)))'''



from math import trunc
num = float(input('Digite um valor :'))
print('O valor digitado foi {}, e sua porção inteira é {}'.format(num, trunc(num)))
