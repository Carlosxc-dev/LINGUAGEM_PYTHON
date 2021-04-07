print('\033[34m-=' * 20)
print(f'\033[35mBANCO CARLOS.H\033[m'.center(40))
print('\033[34m-=\033[m' * 20)
valor = int(input('que valor voce quer sacar? R$ '))
total = valor
ced = 50
totced = 0 
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cedulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('\033[34m-=' * 20)
print('\033[35mVOLTE SEMPRE---BOM DIA\033[m'.center(40))

