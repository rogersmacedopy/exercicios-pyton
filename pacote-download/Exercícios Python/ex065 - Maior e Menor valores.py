#Maior e Menor valores

resp = 'S'
list = []
while resp in 'Ss':
    list.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
print('''A média entre todos os valores é {sum(list) / len(list):.1f}
O maior valor digitado foi {max(list)} e o menor {min(list)}
Foram digitados {len(list)} número''')