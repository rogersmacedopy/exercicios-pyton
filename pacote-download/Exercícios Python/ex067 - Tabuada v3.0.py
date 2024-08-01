#Tabuada v3.0

c = 0
while True:
    t = int(input('Digite um número inteiro que te daremos a sua tabuada: '))
    print('-'*20)
    if t < 0:
        break
    while c < 10:
        c += 1
        print(f'{t} * {c:2} = {t*c}')
    print('-'*20)