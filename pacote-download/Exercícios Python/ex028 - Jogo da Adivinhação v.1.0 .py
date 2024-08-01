#028 - Jogo da Adivinhação v.1.0

from random import randint
from time import sleep
computador = randint(0,5)
print('pensei no número...{}'.format(computador))
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei ?'))
print('Pocessando...')
sleep(3)
if jogador == computador :
    print('Parabens você consegiu me vencer !')
else:
    print('Ganhei, eu pensei no número {} e não no {}!'.format(computador, jogador))

