#011 - Pintando Parede

larg = float(input('largura da parede: '))
alt =  float(input('Digite a altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua ara é de {}m2.'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede você precisará de {}L de tinta.'.format(tinta))
