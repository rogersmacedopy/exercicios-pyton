#040 - Aquele clássico da Média

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('segunda nota do aluno: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f} a nota do aluno é {:.1f} !'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em recuperação! ')
elif média < 5:
    print('O aluno está reprovado! ')
elif média >= 7:
    print('O aluno está aprovado! ')

