from datetime import date
ano = int(input('que ano quer analizar?\nou digite 0 para analizar a ano atual'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} e bissesto'.format(ano))
else:
    print('o ano {} nao e bissesto'.format(ano))
