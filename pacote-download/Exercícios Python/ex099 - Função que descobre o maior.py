#099 - Função que descobre o maior

def maior():
    lista = list()
    up = 0
    while True:
        n = int(input('Digite um número: '))
        if n == 000:
            break
        else:
            lista.append(n)
            if n >= up:
                up = n
            else:
                up = up
    print(lista)
    print(f'Foram ao todo {len(lista)}')
    print(f'O maior valor é {up}')


maior()