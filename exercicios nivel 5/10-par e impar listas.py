num = []
pares = []
impares = []
while True:
    num.append(int(input('digite um valor: ')))
    resp = str(input('continuar? [s/n]'))
    if resp in 'nN':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
'\n'
print(f'a lista completa e {num}')
print(f'a lista de pares e {pares}')
print(f'a lista de impares e {impares}')


