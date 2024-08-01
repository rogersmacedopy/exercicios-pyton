#018 - Seno, Cosseno e Tangente

'''import math
ang = float(input('digite o ângulo que você deseja:'))
sen = math.sin(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
cos = math.cos(math.radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
tag = math.tan(math.radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang,tag))'''

from math import radians, sin, cos, tan
ang = float(input('digite o ângulo que você deseja:'))
sen = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
cos = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
tag = tan(radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tag))
