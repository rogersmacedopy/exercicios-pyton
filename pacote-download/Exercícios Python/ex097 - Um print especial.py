# 097 - Um print especial

def titulo(texto):
    print('~'*len(texto)*2)
    print(texto.center(len(texto)*2,' '))
    print('~'*len(texto)*2)

msg = str.title(input('Informe uma mensagem: '))