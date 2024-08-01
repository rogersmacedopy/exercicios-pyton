#042 - Analisando Triângulos v2.0

'''print('=-' * 20)
print('Analizador de triângulo')
print('=-' * 20)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro seguimento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos a cima podem formar triângulo !')
    if r1 == r2 == r3:
        print('Tiângulo Equilátero')
    if r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('triangulo Isóscelis')
    if r1 != r2 != r3 or r2 != r1 != r3 != r3 != r1 != r2:
        print('Triangulo Escaleno')
else:
    print('Os seguimentos a cima NÃO podem formar triângulos!')'''

l1=float(input('Digite um lado do triângulo: '))
l2=float(input('Digite outro lado do triângulo: '))
l3=float(input('Digite o último lado do triângulo: '))
hip=max([l1, l2, l3])
if hip==l1:
    c1=l2
    c2=l3
elif hip==l2:
    c1=l1
    c2=l3
else:
    c1=l1
    c2=l2
if hip>=(c1+c2):
    print(f'É impossível formar um triângulo de lados {hip}, {c1}, {c2}.')
elif hip>(c1*c1+c2*c2)**0.5:
    angulo='obtusângulo'
elif hip==(c1*c1+c2*c2)**0.5:
    angulo='retângulo'
else:
    angulo = 'acutângulo'
if hip>=(c1+c2):
    c2=1
elif hip==c1 and c1==c2:
    lado='equilátero'
elif hip==c1 or c1==c2 or hip==c2:
    lado='isósceles'
else:
    lado='escaleno'
if hip>=(c1+c2):
    c2=1
else:
    print(f'O triângulo é um triângulo {angulo} e {lado}.')




