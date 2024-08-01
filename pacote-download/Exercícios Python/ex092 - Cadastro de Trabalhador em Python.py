# 092 - Cadastro de Trabalhador em Python

from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: ')).strip().title()
anoNascimento = int(input('Ano de Nascimento: '))
pessoa['idade']  = date.today().year - anoNascimento
if pessoa['idade'] > 16:
    pessoa['nCtps'] = str(input('Número da CTPS (0 - não tem): ')).strip().upper()
    if pessoa['nCtps'] not in '0':
        pessoa['inicioCtps'] = int(input('Ano de Contratação: '))
        if pessoa['inicioCtps'] - anoNascimento >= 16:
                pessoa['salario'] = float(input('Salário: '))
                pessoa['aposentadoria'] = pessoa['inicioCtps'] + 35 - anoNascimento
        else:
            if pessoa['inicioCtps'] != 0:
                del pessoa['inicioCtps']
                print(f'Erro no Ano da Carteira. A Assinatura deve ser a partir de {anoNascimento+16} para poder assinar a CTPS!')
for k, v in pessoa.items():
    print(f" => {k} tem o valor {v}")