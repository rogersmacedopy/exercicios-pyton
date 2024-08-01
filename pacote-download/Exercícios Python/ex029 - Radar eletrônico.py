#029 - Radar eletrônico

velocidade = float(input('Qual é a velocidade do carro ? '))
if velocidade > 80:
    print('Multado, você exedeu o limite de velocidade que era 80km/h')
multa = (velocidade - 80) * 7
print('Você deve pagar uma multa de {:.2}'.format(multa))
print('tenha um bom dia, dirija com segurança !')