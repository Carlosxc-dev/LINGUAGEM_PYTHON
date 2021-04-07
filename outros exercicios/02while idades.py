tot18 = totM = tot20 = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totM += 1
    if sexo == 'F' and idade < 20:
        tot20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('continua [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o total de pessoas +18: e {tot18}')
print(f'o total de mulheres com menos de 20 anos e {tot20}')
print(f'o total de homens sao {totM}')
