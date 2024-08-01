# 022 - Analisador de Textos

nome = str(input('Digite seu nome completo : ')).strip()
print('analizando seu nome...')
print('seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('seu nome tem oa todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
