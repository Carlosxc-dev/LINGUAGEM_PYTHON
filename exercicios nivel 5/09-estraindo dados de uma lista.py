valores = []
while True:
    valores.append(int(input('digite um valor: ')))
    resp = str(input('continuar? [s/n]'))
    if resp in 'nN':
        break
print()
print(f'voce digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'os valores em ordem decrescente sao {valores}')
if 5 in valores:
    print('5 esta na lista ')
else:
    print('5 nao esta')
