from datetime import date

atual = date.today().year
nasc = int(input('digite ano do seu nascimento:  '))
idade = atual - nasc
print('quem nasceu em {} tem {} anos anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('voce tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade 
    print('ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('seu alistamento sera em {} '.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('ja passou {} anos do alistamento'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {}'.format(ano))




