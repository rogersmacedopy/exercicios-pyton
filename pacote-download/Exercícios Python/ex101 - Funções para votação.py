# 101 - Funções para votação

def voto(a):
    from datetime import date
    hoje = date.today().year

    if hoje-a >= 18 and hoje-a <= 65:
        print('VOTO OBRIGATÓRIO')
    elif hoje-a < 16:
        print('VOTO NEGADO')
    else:
        print('VOTO OPCIONAL')

ano = int(input('Digite o ano (aaaa): '))
voto(ano)