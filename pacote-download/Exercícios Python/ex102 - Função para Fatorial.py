# 102 - Função para Fatorial

def fatorial(valor, show=False):
    soma = 1
    for i in range(valor,0,-1):
        if show :
            print(i, end="")
            if i >1:
                print(f' x ', end=" ")
            else:
                print(f" = ",end='')

        soma *= i

    return soma

num = int(input("Deseja sabe o fatorial de qual valor: "))
inter = input("Deseja mostra o calculo?[S/N]").upper()
if inter == "S":
    show = True
else:
    show = False
print(fatorial(num, show=show))
