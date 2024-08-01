#058 - Jogo da Adivinhação v2.0

from random import randint
computador = randint(0, 10)
print('sou seu computador... acabei de penasar em um númeroo entre 0 e 10.')
print('Será que você consegue adivinhar qual foi ?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite ?'))
    palpite += 1
    if jogador == computador:
        cetou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos tente mais uma vez')
print(f'Acertou com {palpite} tentativas!!!')

