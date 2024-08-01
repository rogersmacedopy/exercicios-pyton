# 098 - Função de Contador

from time import sleep
def contagem(inicio, fim, passo):
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo < 0:
        passo += -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        for n in range(inicio - 1, fim):
                        sleep(0.10)
                        print(n + passo, end = ' ')
    else:
        for n in range(inicio, fim - passo, -passo):
            sleep(0.10)
            print(n,end=' ')
    print('FIM!')
contagem(1,10, 1)
contagem(10, 0, 2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('ínicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
contagem(inicio, fim, passo)