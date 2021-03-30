from random import randint
num = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))
print(f'os valores foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\no maior valor sorteado foi {max(num)}')
print(f'o menor valor sorteado foi {min(num)}')


