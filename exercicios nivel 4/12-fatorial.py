n = int(input('fale numero: '))
f = 1
c = n
print('calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))




