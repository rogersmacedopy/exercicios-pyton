#035 - Analisando Triângulo v1.0

print('=-' * 20)
print('Analizador de triângulo')
print('=-' * 20)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro seguimento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos a cima podem formar triângulo !')
else:
    print('Os seguimentos a cima NÃO podem formar triângulos!')
