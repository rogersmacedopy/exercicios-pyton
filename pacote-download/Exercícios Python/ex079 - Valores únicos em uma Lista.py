# 079 - Valores únicos em uma Lista

lista=[]
resposta=""
while resposta in "S":
    num=int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
    else:
        print("Esse numero ja existe")
    resposta=str(input("Deseja continuar? [S/N]")).upper()
    if resposta == "N":
        break
print(sorted(lista))