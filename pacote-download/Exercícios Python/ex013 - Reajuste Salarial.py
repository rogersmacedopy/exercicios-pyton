#013 - Reajuste Salarial

s=float(input(' qual é o valor do salario?'))
r=float(input('valor do reajuste?'))
j=s*r/100
b=s+j
print('seu salario {} reajuste de {}% valor do reajuste {} valor final {}'.format(s,r,j,b))