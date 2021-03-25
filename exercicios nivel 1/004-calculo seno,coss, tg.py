from math import sin, cos, tan, radians
ang = float(input('fale o angulo: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))
print('\n')
print('seno é: {:.2f}\ncosseno é: {:.2f},\ntangente é: {:.2f}'.format(seno, cos, tg))
