prim = int(input('primeiro termo: '))
raz = int(input('razao: '))
dec = prim + (10 - 1) * raz
for c in range(prim, dec + raz, raz):
    print(' {}'.format(c,), end=' ->')
print('acabou')



