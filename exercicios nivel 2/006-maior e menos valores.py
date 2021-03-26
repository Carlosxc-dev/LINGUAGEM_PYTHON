a = int(input('primeiro: '))
b = int(input('segundo: '))
c = int(input('terceiro: '))

menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('o menor e {}'.format(menor))
