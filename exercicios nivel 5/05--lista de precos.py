lista = ('borracha', 1, 'lapis', 1.50, 'caderno', 10, 'tesoura', 5, 'pincel', 2)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-'*40)
