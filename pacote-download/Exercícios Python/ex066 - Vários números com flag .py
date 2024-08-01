# Vários números com flag

soma=0
msg=0
while msg!=999:
    msg=int(input("Digite um valor [999 para parar]: "))
    if msg==999:
        break
    soma=soma+msg
print("A Soma dos valores é {}".format(soma))