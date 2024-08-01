#Progressão Aritmética v2.0

n1 = int(input ('Digite o primeiro termo da PA'))
n2 = int(input('Digite a raiz:'))
print (n1, end = ' ')

decimo = n1 + (10-1) * n2
while n1 < decimo:
    n1 += n2
    print('{} '.format(n1), end=' ')